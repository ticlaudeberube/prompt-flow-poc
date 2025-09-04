# MCP Servers Configuration

This project uses Model Context Protocol (MCP) servers to enhance development capabilities.

## Configured Servers

### filesystem
- **Purpose**: File operations within the project
- **Path**: `d:\fichiers de claude\workspace\prompt-flow-poc`
- **Usage**: Read/write project files, manage flow configurations

### git
- **Purpose**: Version control operations
- **Repository**: Current project directory
- **Usage**: Track changes, manage commits, view history

### azure
- **Purpose**: Azure service integration
- **Requirements**: Azure credentials in environment variables
- **Usage**: Manage Azure resources, deploy flows, access Azure AI services

### sqlite
- **Purpose**: Local data storage
- **Path**: `d:\fichiers de claude\workspace\prompt-flow-poc\data`
- **Usage**: Store flow results, metrics, experiment data

### memory
- **Purpose**: Persistent context across conversations
- **Usage**: Maintain state between flow iterations

## Setup

1. Copy `.env.example` to `.env`
2. Fill in Azure credentials
3. Create `data/` directory for SQLite: `mkdir data`
4. MCP servers will auto-start when needed

## Environment Variables

Required for Azure MCP server:
- `AZURE_SUBSCRIPTION_ID`
- `AZURE_TENANT_ID` 
- `AZURE_CLIENT_ID`
- `AZURE_CLIENT_SECRET`