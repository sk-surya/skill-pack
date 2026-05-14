#!/usr/bin/env python3
"""
Quick validation script for skills.
"""

from pathlib import Path
import re
import sys


YAML_BLOCK_SCALAR_INDICATORS = ("|", ">", "|-", ">-", "|+", ">+")
MIXED_VALUES_ERROR_MESSAGE = "Mixed list and mapping values are not supported for key"
TODO_PATTERN = re.compile(r"\[?TODO[:\]]", re.IGNORECASE)


def extract_frontmatter(content):
    """Extract raw YAML frontmatter from a SKILL.md file."""
    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", content, re.DOTALL)
    if not match:
        return None
    return match.group(1)


def parse_frontmatter(frontmatter):
    """Parse the subset of YAML used by skill frontmatter."""
    data = {}
    lines = frontmatter.splitlines()
    index = 0

    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue

        if line.startswith((" ", "\t")):
            return None, f"Top-level keys cannot be indented: {line.strip()}"

        if ":" not in line:
            return None, f"Invalid frontmatter line: {line}"

        parts = line.split(":", 1)
        if len(parts) != 2:
            return None, f"Invalid frontmatter line: {line}"

        key, raw_value = parts
        key = key.strip()
        value = raw_value.strip()

        if not key:
            return None, "Frontmatter key cannot be empty"

        if value in YAML_BLOCK_SCALAR_INDICATORS:
            block_lines = []
            index += 1
            while index < len(lines):
                next_line = lines[index]
                if next_line.startswith("  "):
                    block_lines.append(next_line[2:])
                    index += 1
                    continue
                if not next_line.strip():
                    block_lines.append("")
                    index += 1
                    continue
                break
            data[key] = "\n".join(block_lines).strip()
            continue

        if not value:
            list_items = []
            nested_values = {}
            index += 1
            while index < len(lines):
                next_line = lines[index]
                if not next_line.strip():
                    index += 1
                    continue
                if next_line.startswith("  - "):
                    if nested_values:
                        return None, f"{MIXED_VALUES_ERROR_MESSAGE} '{key}'"
                    list_items.append(next_line[4:].strip())
                    index += 1
                    continue
                if next_line.startswith("  ") and ":" in next_line[2:]:
                    if list_items:
                        return None, f"{MIXED_VALUES_ERROR_MESSAGE} '{key}'"
                    nested_key, nested_raw_value = next_line[2:].split(":", 1)
                    nested_values[nested_key.strip()] = nested_raw_value.strip().strip("\"'")
                    index += 1
                    continue
                if next_line.startswith((" ", "\t")):
                    return None, f"Unsupported nested frontmatter value for key '{key}'"
                break
            if list_items:
                data[key] = list_items
            elif nested_values:
                data[key] = nested_values
            else:
                data[key] = ""
            continue

        data[key] = value.strip("\"'")
        index += 1

    return data, None


def validate_skill(skill_path):
    """Validate a skill directory against current Copilot-friendly conventions."""
    skill_path = Path(skill_path)

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, "SKILL.md not found"

    if (
        not re.match(r"^[a-z0-9-]+$", skill_path.name)
        or skill_path.name.startswith("-")
        or skill_path.name.endswith("-")
        or "--" in skill_path.name
    ):
        return False, f"Directory name '{skill_path.name}' should be lowercase hyphen-case"

    content = skill_md.read_text()
    if not content.startswith("---"):
        return False, "No YAML frontmatter found"

    frontmatter = extract_frontmatter(content)
    if frontmatter is None:
        return False, "Invalid frontmatter format"

    metadata, error = parse_frontmatter(frontmatter)
    if error:
        return False, error

    name = metadata.get("name", "").strip()
    description = metadata.get("description", "").strip()

    if not name:
        return False, "Missing 'name' in frontmatter"
    if not description:
        return False, "Missing 'description' in frontmatter"

    if not re.match(r"^[a-z0-9-]+$", name):
        return False, f"Name '{name}' should be hyphen-case (lowercase letters, digits, and hyphens only)"
    if name.startswith("-") or name.endswith("-") or "--" in name:
        return False, f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens"
    if name != skill_path.name:
        return False, f"Frontmatter name '{name}' should match directory name '{skill_path.name}'"
    if TODO_PATTERN.search(description):
        return False, "Description still contains TODO placeholder text"

    allowed_tools = metadata.get("allowed-tools")
    if allowed_tools:
        if isinstance(allowed_tools, str):
            allowed_tools = [allowed_tools]
        if not isinstance(allowed_tools, list) or not all(
            isinstance(tool, str) and tool.strip() for tool in allowed_tools
        ):
            return False, "allowed-tools must be a non-empty string or list of non-empty strings"

    return True, "Skill is valid!"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quick_validate.py <skill_directory>")
        sys.exit(1)
    
    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)
