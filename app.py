import argparse
from html import escape
import pandas as pd
from pathlib import Path

def metrics(df):
    d=df.copy()
    required=['impressions','likes','comments','shares']
    missing=set(required)-set(d.columns)
    if missing: raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
    for c in required:
        d[c]=pd.to_numeric(d[c],errors='raise')
        if (d[c]<0).any(): raise ValueError('Negative counts')
    d['engagements']=d.likes+d.comments+d.shares;d['rate_pct']=100*d.engagements/d.impressions.where(d.impressions>0)
    return d

def report_html(d):
    total=int(d.impressions.sum()); engagements=int(d.engagements.sum())
    rate=100*engagements/total if total else 0
    top=d.sort_values('engagements',ascending=False).head(8).copy()
    labels=[escape(str(x)) for x in (top['post'] if 'post' in top else top.index)]
    peak=max(top.engagements.max(),1) if len(top) else 1
    bars=''.join(f'<div class="bar-row"><span>{label}</span><i style="width:{100*v/peak:.1f}%"></i><b>{v:,}</b></div>' for label,v in zip(labels,top.engagements))
    table=d.sort_values('engagements',ascending=False).to_html(index=False,escape=True,classes='data-table',border=0)
    return f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SNS analytics report</title><style>
*{{box-sizing:border-box}}body{{margin:0;background:#f5f7fb;color:#172033;font:15px/1.5 system-ui,-apple-system,sans-serif}}main{{max-width:1080px;margin:auto;padding:48px 24px}}h1{{margin:0;font-size:2.2rem}}.sub{{color:#64748b;margin:.4rem 0 2rem}}.cards{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:24px}}.card,.panel{{background:white;border:1px solid #e6eaf0;border-radius:16px;padding:20px;box-shadow:0 8px 24px #17203308}}.card span{{display:block;color:#64748b;font-size:.85rem}}.card strong{{font-size:1.8rem}}.panel{{margin-top:20px}}h2{{font-size:1.05rem;margin:0 0 16px}}.bar-row{{display:grid;grid-template-columns:minmax(110px,2fr) minmax(70px,5fr) auto;gap:12px;align-items:center;margin:10px 0}}.bar-row span{{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}.bar-row i{{height:10px;border-radius:99px;background:linear-gradient(90deg,#6366f1,#22c55e)}}.bar-row b{{font-variant-numeric:tabular-nums}}.data-table{{width:100%;border-collapse:collapse}}.data-table th{{text-align:left;color:#64748b;font-size:.8rem;text-transform:uppercase;letter-spacing:.04em}}.data-table td,.data-table th{{padding:11px 8px;border-bottom:1px solid #edf0f5}}@media(max-width:600px){{main{{padding:28px 16px}}.cards{{grid-template-columns:1fr}}.panel{{overflow:auto}}}}
</style><main><h1>SNS analytics</h1><p class="sub">Offline engagement performance report</p><section class="cards"><div class="card"><span>Impressions</span><strong>{total:,}</strong></div><div class="card"><span>Engagements</span><strong>{engagements:,}</strong></div><div class="card"><span>Engagement rate</span><strong>{rate:.2f}%</strong></div></section><section class="panel"><h2>Top posts by engagement</h2>{bars or '<p>No posts available.</p>'}</section><section class="panel"><h2>All posts</h2>{table}</section></main></html>'''

def main():
    p=argparse.ArgumentParser(description='Create a polished offline SNS analytics report.');p.add_argument('input');p.add_argument('output');a=p.parse_args()
    Path(a.output).write_text(report_html(metrics(pd.read_csv(a.input))),encoding='utf-8')
if __name__=='__main__': main()
