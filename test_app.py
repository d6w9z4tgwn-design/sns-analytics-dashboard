import unittest,pandas as pd
from app import metrics
class Test(unittest.TestCase):
 def test_rate(self):
  d=metrics(pd.DataFrame({'impressions':[100,0],'likes':[5,0],'comments':[2,0],'shares':[3,0]}));self.assertEqual(d.rate_pct[0],10);self.assertTrue(pd.isna(d.rate_pct[1]))
