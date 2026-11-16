import argparse,pandas as pd
from pathlib import Path

def metrics(df):
    d=df.copy()
    for c in ['impressions','likes','comments','shares']:
        d[c]=pd.to_numeric(d[c],errors='raise')
        if (d[c]<0).any(): raise ValueError('Negative counts')
    d['engagements']=d.likes+d.comments+d.shares;d['rate_pct']=100*d.engagements/d.impressions.where(d.impressions>0)
    return d

def main():
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');a=p.parse_args();d=metrics(pd.read_csv(a.input));total=d.impressions.sum();rate=100*d.engagements.sum()/total if total else 0
    html='<!doctype html><meta charset="utf-8"><title>SNS report</title><style>body{font:16px system-ui;margin:3rem;background:#f5f7fa}table{border-collapse:collapse;background:white}td,th{padding:12px;border:1px solid #ddd}</style><h1>SNS analytics</h1>'+f'<p>Impressions: {total:,} | Engagement rate: {rate:.2f}%</p>'+d.sort_values('engagements',ascending=False).to_html(index=False,escape=True)
    Path(a.output).write_text(html,encoding='utf-8')
if __name__=='__main__': main()
