# win-loss-analysis

Python CLI for analysing CRM deal data to surface win rates, loss patterns, and cycle lengths by segment. Built to answer the question: which verticals and deal sizes are we actually good at closing?

## Architecture

```
src/
  loader.py       load_deals() — reads CSV export from CRM
  analyser.py     win_rate_by_segment(), loss_reasons(), win_rate_trend(), cycle_length_by_segment()
  reporter.py     print_* functions — tabular terminal output
  main.py         entry point — runs full report
data/
  deals.csv       sample deals (anonymised)
tests/
  test_analyser.py
```

## Quickstart

```bash
pip install -r requirements.txt
python -m src.main
pytest tests/
```

## Sample output

```
  Win Rate by Vertical
  Segment                    Win %
  -------------------------- -------
  fintech                     78.6%  ###############
  saas                        62.3%  ############
  marketplace                 55.0%  ###########
  healthtech                  40.0%  ########

  Loss Reasons  (n=18)
  Reason                       Count   Share
  ----------------------------  ------  ------
  pricing                           7   38.9%
  no_budget                         5   27.8%
  competitor                        4   22.2%
  no_champion                       2   11.1%
```

## Motivation

After exporting 3 months of closed deals from our CRM I realised we had no structured view of which segments were converting. This script replaced a manual spreadsheet and made it easy to run the analysis on any fresh export.

## Future work

- Add deal source (inbound vs outbound) as a segmentation dimension
- Export summary to CSV for BI tool ingestion
- Add statistical significance test for win rate differences between segments
