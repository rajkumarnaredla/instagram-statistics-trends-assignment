INSTAGRAM STATISTICS AND TRENDS

CONTENTS
four_charts/Instagram_Assignment_Bar_Pie_Line.pdf: two-page report with a bar chart, pie chart, line plot and heatmap.
instagram_country_usage.csv: 52 countries/territories. Each row is a market, not a person.
instagram_age_gender.csv: six global age groups, split by the two gender categories published by the source. These are advertising-audience percentages, not time spent.
build_four_chart_report.py: Python analysis and report generation.
four_charts/*.png: the four generated chart images.

IMPORTANT DEFINITIONS
monthly_minutes: average minutes spent per active Instagram Android-app user in November 2024.
monthly_sessions: average number of Instagram Android-app openings per active user in November 2024.
monthly_hours: monthly_minutes divided by 60.
daily_minutes_derived: monthly_minutes divided by the 30 calendar days in November 2024. This is a calculated calendar-day average, not a separately measured average per active day.
female_pct and male_pct: published global advertising-audience shares by age and gender, from the February 2025 report.
combined_pct: female_pct plus male_pct in the same age group.

FINDINGS
Turkey ranks first among the 52 reported markets at 32 hours 36 minutes monthly per active Android-app user. This is 65.2 minutes per calendar day by division by 30.
India ranks fifth at 20 hours 27 minutes; the UK records 8 hours 56 minutes.
Ages 25-34 represent the largest combined audience share, 33.0%, followed by ages 18-24 at 31.6%.
The data do not establish which age group spends the most time on Instagram. They also do not provide time by age within each country. Do not merge these tables to invent those results.
Monthly openings and monthly time across the 52 markets have Pearson correlation 0.8859105988. This is an association between market averages, not an individual-level or causal finding.

SOURCE AND TRANSCRIPTION
DataReportal, We Are Social and Meltwater (2025), Digital 2025: Global Overview Report, February.
Page 449: Instagram advertising-audience profile (Meta advertising resources; Kepios analysis).
Page 451: time spent using Instagram mobile app (data.ai, a Sensor Tower company).
Page 452: monthly Instagram app sessions per user (data.ai).
Public report: https://wearesocial.com/wp-content/uploads/2025/02/GDR-2025-v2.pdf
Downloaded copy: https://learn.meltwater.com/rs/814-WJU-189/images/2025_Kepios_Digital_Global_Overview_Report.pdf
Accessed 5 November 2026. These are historical figures, not latest 2026 rankings.
Country values were extracted from the PDF text and inspected against the source charts. The time and openings tables were matched using their country labels. The WORLDWIDE benchmark was excluded from the 52 country rows. No missing or duplicate country rows were present. Countries/territories use source labels, including TURKEY, U.K. and HONG KONG.
Worldwide benchmarks: 16h 13m monthly and 331.8 monthly sessions; the source excludes China from the worldwide figures.
The unweighted average across markets is not a global average across users.

REPRODUCE
Keep build_four_chart_report.py and both CSV files in the same folder.
Required Python packages: pandas, numpy, matplotlib, reportlab.
Install if needed: python -m pip install pandas numpy matplotlib reportlab
Set the report identity before generating (optional; fields remain fillable):
PowerShell: $env:INSTAGRAM_STUDENT_NAME="Your Name"; $env:INSTAGRAM_STUDENT_NUMBER="Your Number"
Run: python build_four_chart_report.py
Outputs appear in a four_charts folder.

BEFORE SUBMITTING
Read and understand the report. Confirm the name and student-number fields before submitting. Check the full Canvas rubric and any separate code or Git requirements. The supplied screenshots specified three plot categories and a two-page report, but did not include the full marking rubric.
This analysis, report and code were prepared with AI assistance. Follow your university's permitted-use and disclosure requirements. No plagiarism or AI-detector outcome is guaranteed.
