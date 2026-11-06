from pathlib import Path
import os
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor,white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'four_charts';OUT.mkdir(exist_ok=True)
student_name=os.environ.get('INSTAGRAM_STUDENT_NAME','').strip()
student_number=os.environ.get('INSTAGRAM_STUDENT_NUMBER','').strip()
d=pd.read_csv(ROOT/'instagram_country_usage.csv');a=pd.read_csv(ROOT/'instagram_age_gender.csv')
assert len(d)==52 and d.country.nunique()==52 and not d.isna().any().any()
assert np.isclose(a.combined_pct.sum(),100)
r=d.monthly_minutes.corr(d.monthly_sessions)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
def save(f,name):
 f.tight_layout(pad=.8);f.savefig(OUT/name,dpi=260);plt.close(f)
b=pd.concat([d.nlargest(5,'monthly_minutes'),d[d.country=='U.K.']]).iloc[::-1]
f,ax=plt.subplots(figsize=(7.2,2.3));ax.barh(b.country,b.monthly_hours,color=['#94a7b9' if n=='U.K.' else '#7452aa' for n in b.country],height=.65)
for j,(_,row) in enumerate(b.iterrows()):ax.text(row.monthly_hours+.35,j,f'{int(row.monthly_minutes)//60}h {int(row.monthly_minutes)%60:02d}m',va='center',fontsize=10)
ax.set(xlabel='Monthly hours per active Instagram Android-app user',xlim=(0,38));save(f,'01_Instagram_Bar_Chart.png')
colors=['#7452aa','#386da6','#2b928c','#c48a35','#b85d79','#85929b']
f,ax=plt.subplots(figsize=(7.2,2.7));wedges,_,texts=ax.pie(a.combined_pct,colors=colors,autopct=lambda pct: f'{pct:.1f}%' if pct>=6 else '',startangle=90,counterclock=False,pctdistance=.77,textprops={'fontsize':10,'color':'white'},wedgeprops={'edgecolor':'white','linewidth':1.5});ax.legend(wedges,[f'{age} years ({pct:.1f}%)' for age,pct in zip(a.age_group,a.combined_pct)],loc='center left',bbox_to_anchor=(1,.5),frameon=False,title='Age group');ax.set_aspect('equal');save(f,'02_Instagram_Pie_Chart.png')
f,ax=plt.subplots(figsize=(7.2,2.6));x=np.arange(len(a));ax.plot(x,a.female_pct,marker='o',color='#a23c79',label='Female');ax.plot(x,a.male_pct,marker='s',color='#386da6',label='Male');ax.set_xticks(x,a.age_group);ax.set(xlabel='Age group (ordered categories, not a time series)',ylabel='Share of reported audience (%)',ylim=(0,21));ax.legend(frameon=False);ax.grid(alpha=.18);save(f,'03_Instagram_Line_Plot.png')
f,ax=plt.subplots(figsize=(7.2,2.4));matrix=np.array([[1,r],[r,1]]);im=ax.imshow(matrix,cmap='Purples',vmin=-1,vmax=1,aspect='auto');labels=['Monthly time','Monthly openings'];ax.set_xticks([0,1],labels);ax.set_yticks([0,1],labels)
for i in range(2):
 for j in range(2):ax.text(j,i,f'{matrix[i,j]:.3f}',ha='center',va='center',color='white',fontsize=15)
f.colorbar(im,ax=ax,pad=.025,label='Pearson correlation',ticks=[-1,0,1]);save(f,'04_Instagram_Heatmap.png')
fonts=Path(matplotlib.get_data_path())/'fonts/ttf'
for name,file in [('Body','DejaVuSans.ttf'),('Body-Bold','DejaVuSans-Bold.ttf'),('Body-Oblique','DejaVuSans-Oblique.ttf')]:pdfmetrics.registerFont(TTFont(name,str(fonts/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Body-Bold',italic='Body-Oblique',boldItalic='Body-Bold')
style=ParagraphStyle('body',fontName='Body',fontSize=10,leading=13.1,textColor=HexColor('#233241'));small=ParagraphStyle('small',parent=style,fontSize=8.4,leading=10.8)
W,H=A4;c=canvas.Canvas(str(OUT/'Instagram_Assignment_Bar_Pie_Line.pdf'),pagesize=A4);c.setTitle('Instagram: time spent and audience profile')
def para(t,y,sty=style):
 p=Paragraph(t,sty);_,h=p.wrap(W-84,800);p.drawOn(c,42,y-h);return y-h-7
def heading(t,y):
 c.setFillColor(HexColor('#67429c'));c.setFont('Body-Bold',11);c.drawString(42,y-11,t);return y-22
def chart(n,y,h):
 c.drawImage(str(OUT/n),42,y-h,width=W-84,height=h,mask='auto',preserveAspectRatio=True,anchor='c');return y-h-3
def footer(n):
 c.setStrokeColor(HexColor('#d9d2e5'));c.line(42,35,W-42,35);c.setFillColor(HexColor('#5b6470'));c.setFont('Body',8);c.drawString(42,22,'Statistics and trends | Historical Instagram data');c.drawRightString(W-42,22,f'{n} / 2')
c.setFillColor(HexColor('#33244c'));c.setFont('Body-Bold',18);c.drawString(42,802,'Instagram: time spent and');c.drawString(42,779,'audience profile')
c.setFont('Body',9);c.drawString(42,757,'Name:');c.drawString(310,757,'Student number:')
for name,x,w,value in [('student_name',76,220,student_name),('student_number',395,158,student_number)]:c.acroForm.textfield(name=name,x=x,y=750,width=w,height=19,value=value,borderWidth=.5,borderColor=HexColor('#b6a8c8'),fillColor=white,textColor=HexColor('#233241'),fontSize=10)
y=para('This report examines Instagram time spent in 52 countries and territories and its global age profile using published tables in <i>Digital 2025</i> [1]. Usage estimates cover active Android-app users in November 2024; demographic shares come from the report\'s early-2025 advertising data. Country labels were matched, hours converted to minutes, and the worldwide row excluded from market statistics. No market rows were missing or duplicated.',737)
y=heading('1. Bar chart: monthly time spent by market',y)
y=chart('01_Instagram_Bar_Chart.png',y,153)
y=para('<b>Figure 1.</b> Top five markets, with the UK added for comparison. Turkey led the 52 reported markets at 32h 36m per user, followed by Brazil at 23h 35m. India ranked fifth at 20h 27m; the UK recorded 8h 56m. Across all markets, the mean was 11.72 hours, the median 10.24 and the standard deviation 5.11. The larger mean reflects the upper tail. These unweighted market statistics are not global user averages.',y)
y=heading('2. Pie chart: age composition of the audience',y)
y=chart('02_Instagram_Pie_Chart.png',y,163)
y=para('<b>Figure 2.</b> Female and male shares were added within each age group. Ages 25-34 formed the largest share (33.0%), just above ages 18-24 (31.6%). Together they accounted for 64.6%. Ages 65+ contributed 3.3%. These are shares of the reported advertising audience, not minutes spent or the percentage of each age group using Instagram. The figures cannot identify which age group spends the longest on the app.',y)
assert y>40,y
footer(1);c.showPage()
y=heading('3. Line plot: age profiles by reported gender',802)
y=chart('03_Instagram_Line_Plot.png',y,173)
y=para('<b>Figure 3.</b> Both profiles peaked at ages 25-34: 18.4% for men and 14.6% for women. The male share was larger in the three younger groups, while the female share was larger from age 45 onwards. Summed shares were 52.4% male and 47.6% female. Lines connect ordered age categories only; they do not represent change over time, equal age intervals or measured values between groups.',y)
y=heading('4. Heatmap: app openings and monthly time',y)
y=chart('04_Instagram_Heatmap.png',y,153)
y=para('<b>Figure 4.</b> Across the 52 markets, monthly openings and monthly time had a strong positive Pearson correlation (r = 0.886). The diagonal values are 1 because each measure is compared with itself. Total time depends partly on opening frequency and session duration, so the association is unsurprising. Country-level averages do not establish individual behaviour or causation.',y)
y=heading('Conclusion and limitations',y)
y=para('Turkey had the highest average time in the listed markets, and ages 25-34 formed the largest reported audience group. Usage excludes iPhone and browser activity. Advertising reach is not identical to active users, and reported ages may be inaccurate. Only female/male demographic categories were available; under-18 gender splits were absent. The time and demographic tables cover different periods and populations, so they were analysed separately. Results describe a historical snapshot, not current global rankings.',y)
y=heading('Data source',y)
y=para('[1] DataReportal, We Are Social and Meltwater (2025). <i>Digital 2025: Global Overview Report</i>, February. Page 449: age/gender shares (Meta advertising resources; Kepios). Pages 451-452: monthly time and openings (data.ai / Sensor Tower). Accessed 5 November 2026. Graphs redrawn and summaries calculated from these tables.<br/><link href="https://wearesocial.com/wp-content/uploads/2025/02/GDR-2025-v2.pdf" color="#67429c">https://wearesocial.com/wp-content/uploads/2025/02/GDR-2025-v2.pdf</link>',y,small)
assert y>40,y
footer(2);c.save();print('Created two-page report. Final text position:',y)
