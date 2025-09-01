## Copilot Usage Guidelines

When using GitHub Copilot in this Python Azure + Prompt Flow project:

- **Follow best practices** for Python, Azure SDKs, and Prompt Flow tools.
- **Do not include sensitive information** (such as secrets, keys, or credentials) in code suggestions.
- **Review and test all Copilot-generated code** before merging or deploying.
- **Prefer official Azure and Prompt Flow documentation** for complex workflows.
- **Ensure code is compatible** with project dependencies listed in `pyproject.toml`.
- **Document any Copilot-generated code** with clear comments if logic is non-obvious.
- **Avoid generating code that violates licenses or copyrights.**

For more details, see [GitHub Copilot documentation](https://docs.github.com/en/copilot).

# Copilot Python Rules

These rules help ensure that GitHub Copilot suggestions for Python code in this Azure + Prompt Flow project are safe, maintainable, and effective.

## General Python Rules

- Follow [PEP 8](https://peps.python.org/pep-0008/) style guidelines.
- Use clear, descriptive variable and function names.
- Write modular, reusable functions and classes.
- Add docstrings to all public functions, classes, and modules.
- Avoid using deprecated Python features or libraries.
- Prefer built-in Python types and libraries when possible.

## Azure SDK Rules

- Use official Azure SDKs and follow their documentation.
- Handle exceptions and errors gracefully.
- Do not hardcode secrets, credentials, or connection strings.
- Use environment variables or Azure Key Vault for sensitive data.

## Prompt Flow Rules

- Use the latest stable version of `promptflow-tools`.
- Document custom flows and components clearly.
- Validate input and output data for flows.
- Follow best practices for prompt engineering.

## Testing and Quality

- Write unit tests for new features and functions.
- Use type hints where appropriate.
- Review and test Copilot-generated code for quality and security.
- Ensure code coverage meets project standards.
- Use linters and formatters to maintain code quality.

## Security Best Practices

- Regularly update dependencies to address security vulnerabilities.
- Use tools like `bandit` or `safety` to scan for security issues in Python code.
- Avoid using insecure functions or patterns (e.g., `eval`, unsanitized input).

## Documentation

- Update documentation when adding new features or flows.
- Include usage examples for complex functions or flows.
- Maintain a changelog for major updates.

## Collaboration

- Communicate Copilot-generated changes in pull requests.
- Tag reviewers for Copilot-assisted code.
- Encourage feedback on Copilot usage and suggestions.

## Accessibility & Inclusivity

- Write code and documentation that is clear and accessible to all contributors.
- Avoid jargon or abbreviations
