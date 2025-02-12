#!/usr/bin/env python3
from bs4 import BeautifulSoup
import os

# Limit amount of returns
limit = 150

# Get script dir.
script_dir = os.path.dirname(os.path.abspath(__file__))

# Read the HTML file
with open(f'{script_dir}/Scanner.html', "r", encoding="utf-8") as f:
    html = f.read()

# Parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Find all containers for a crypto pair’s data.
# (Based on a quick glance the rows seem to be in divs with class "w-full".)
rows = soup.find_all("div", class_="w-full")

pairs_data = []
strip_list = [
    'class="flex items-center justify-between truncate"><span class="text-primary">',
    'class="flex items-center justify-between truncate"><span class="text-secondary">',
    '</span></',
    '</',
    '>',
    'class="text-sm number truncate"',
    'class="text-xs thin number truncate"',
    'class="number text-xs truncate"',
    'class="text-xs number truncate"',
    'class="text-right text-sm number text-natural-400"',
    'class="text-right text-sm number text-natural-200"',
    'class="text-right text-sm number text-positive"',
    'class="text-natural-400"<span<!--$--',
    'class="text-positive"<span<!--$--',
    'class="text-natural-200"<span<!--$--',
    '<!--/--',
    'class="number text-center text-natural-400"',
    'class="number text-center text-natural-200"',
    'class="number text-center text-positive"',
    'class="number text-center"',
    'class="number text-center text-positive-focus"',
    '<!--$--'
]
# Print header
f = open(f'{script_dir}/output.csv', "w")
f.write('Coin X, Coin Y,Volume Coin X,Volume Coin Y,Updated,Spread,Strategy,normalised spread (ZSCORE),Rolling ZScore,Profile (Clustering Analysis),X | Y (Conditional Likelihood),Y | X (Conditional Likelihood),Copula-based Correlation,Cointegration Jn (Johansen Test),Cointegration EG (Engle-Granger Test),Hurst Exponent,Half Life,0sigma,2sigma,Coin X Annualized Volatility,Coin Y Annualized Volatility,VaR (Value at Risk @ 99%),CVaR (Conditional Value at Risk @ 99%),MDD (Maximum Drawdown),Net Return (Net Backtest Return),Sharpe (Sharpe Ratio)\n')
counter = 1
for row in rows:
    if counter > limit:
        continue
    rowx = str(row).split('div')
    lines = []
    for r in rowx:
        for string in strip_list:
            r = r.strip()
            r = r.replace(string, '')
        lines += [r]
    # set values
    if len(lines) == 165:
        counter += 1
        coin1 = lines[4]
        coin2 = lines[6]
        volume_coin1 = lines[10]
        volume_coin2 = lines[12]
        updated = f'{lines[20]} {lines[22]}'
        # Spread
        if lines[26] == 'static':
            spread = 'Static AutoRegressive Moving Average'
        elif lines[26] == 'dynamic':
            spread = 'Dynamic - Kalman Filter'
        elif lines[26] == 'ou':
            spread = 'Ornstein-Uhlenbeck'
        elif lines[26] == 'none':
            spread = 'Not applicable'
        else:
            exit('Error Spread!')
        # Strategy
        if lines[28] == 'spread':
            strategy = 'Spread'
        elif lines[28] == 'zscore_roll':
            strategy = 'Rolling Z-Score'
        elif lines[28] == 'copula':
            strategy = 'Copula'
        else:
            exit('Error Strategy!')
        # Z-score
        normalised_spread =lines[33]
        rolling_zscore =  lines[39]
        # Profile
        if 'positive' in lines[46]:
            profile = 'true'
        else:
            profile = 'false'
        # Copula
        x_y_c_l = lines[53]
        y_x_c_l = lines[59]
        correlation = lines[67]
        # Stationary
        if 'positive' in lines[75]:
            cointegration_jn = 'true'
        else:
            cointegration_jn = 'false'
        if 'positive' in lines[77]:
            cointegration_eg = 'true'
        else:
            cointegration_eg = 'false'
        hurst = lines[91]
        half_live = lines[99]
        sigma_0 = lines[107]
        sigma_2 = lines[113]
        # volatility and risk
        coin1_a_v = lines[120]
        coin2_a_v = lines[122]
        var = lines[127]
        cvar = lines[135]
        mdd = lines[143]
        # Reward
        net_return = lines[151]
        sharpe = lines[158]
        f.write(f'{coin1},{coin2},{volume_coin1},{volume_coin2},{updated},{spread},{strategy},{normalised_spread},{rolling_zscore},{profile},{x_y_c_l},{y_x_c_l},{correlation},{cointegration_jn},{cointegration_eg},{hurst},{half_live},{sigma_0},{sigma_2},{coin1_a_v},{coin2_a_v},{var},{cvar},{mdd},{net_return},{sharpe}\n')
f.close