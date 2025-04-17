# AWS Cloudtrail Parser

Parser tool written with Python to parse AWS logs from Cloudtrail data source  

## Requirements

| Name | Version |
|------|-------------|
| <a name="eksctl"></a> [pip3](pip3) | 20.2.4 
| <a name="eksctl"></a> [Python](Python) | 3.6.7

## Usage
```bash
# Install requirements
cd parser
pip3 install -r req.txt

# Run Parser
python3 parser.py -f <log file location>
```

## Rollback Process
If you need to rollback to a previous state after parsing:

1. The parser automatically creates backup files with `.bak` extension before processing
2. To rollback, simply rename the backup file by removing the `.bak` extension
3. Example rollback command:
```bash
mv your_logfile.json.bak your_logfile.json
```

## GitHub Actions Rollback Process

The `rollback.yml` workflow provides an automated way to revert deployments to a previous stable state. Here's how it works:

1. **Trigger**: The workflow can be triggered:
   - Manually via GitHub UI (workflow_dispatch)
   - Automatically when a deployment fails
   - Through API calls to GitHub Actions

2. **Rollback Steps**:
   - Identifies the last successful deployment commit
   - Reverts the application state to that commit
   - Updates the deployment status in GitHub
   - Notifies relevant teams via Slack

3. **Usage**:
   ```bash
   # Manual trigger via GitHub CLI
   gh workflow run rollback.yml -f environment=production
   ```

4. **Parameters**:
   - `environment`: (Required) Target environment (production/staging)
   - `version`: (Optional) Specific version to rollback to

5. **Monitoring**:
   - Rollback status can be monitored in GitHub Actions UI
   - Slack notifications provide real-time updates
   - Deployment history is preserved for audit purposes

⚠️ **Note**: Ensure you have appropriate permissions before triggering a rollback.
