name: Metabase to Telegram

on:
  schedule:
    # каждый день в 9:00 МСК (UTC+3 → UTC+0 нужно вычесть 3 часа)
    - cron: '0 0 * * *'
  workflow_dispatch: # позволяет запускать вручную

jobs:
  run-script:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pandas requests openpyxl

      - name: Run Metabase script
        env:
          METABASE_URL: ${{ secrets.METABASE_URL }}
          METABASE_USER: ${{ secrets.METABASE_USER }}
          METABASE_PASSWORD: ${{ secrets.METABASE_PASSWORD }}
          TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
          CHAT_ID: ${{ secrets.TELEGRAM_CHAT_ID }}
        run: |
          python metabase_to_telegram.py

