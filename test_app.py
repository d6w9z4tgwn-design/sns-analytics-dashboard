import unittest,pandas as pd
from app import metrics,report_html
class Test(unittest.TestCase):
 def test_rate(self):
  d=metrics(pd.DataFrame({'impressions':[100,0],'likes':[5,0],'comments':[2,0],'shares':[3,0]}));self.assertEqual(d.rate_pct[0],10);self.assertTrue(pd.isna(d.rate_pct[1]))
 def test_report_has_summary(self):
  d=metrics(pd.DataFrame({'impressions':[100],'likes':[5],'comments':[2],'shares':[3]}))
  html=report_html(d);self.assertIn('Engagement rate',html);self.assertIn('10.00%',html)
