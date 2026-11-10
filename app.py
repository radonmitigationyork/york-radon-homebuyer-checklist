import streamlit as st
from html import escape

st.set_page_config(
    page_title="Buying a Home in York, PA? Check the Radon Test Before Closing",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown('''<style>
[data-testid="stHeader"] {background: transparent;}
.block-container {max-width: 850px; padding-top: 2.4rem; padding-bottom: 4rem;}
html, body, [class*="css"] {font-family: Arial, Helvetica, sans-serif;}
h1, h2, h3 {color:#173b46; letter-spacing:-.02em;}
h1 {font-size: 2.35rem !important; line-height:1.18 !important;}
h2 {font-size:1.48rem !important; margin-top:1.5rem !important;}
p, li {line-height:1.76;}
a {color:#087d80;}
.kicker {color:#087f74; font-size:.8rem; font-weight:700; letter-spacing:.12em; text-transform:uppercase;}
.lead {font-size:1.1rem; color:#485d68; line-height:1.75;}
.notice {background:#e9f5f2; border-left:4px solid #118676; border-radius:5px; padding:17px 20px; margin:24px 0;}
.footer {margin-top:32px; background:#173b46; border-radius:12px; padding:25px; color:white;}
.footer h3 {color:white; margin-top:0;}
.footer p {color:#d8e5e7;}
.profile-links {display:flex; flex-wrap:wrap; gap:9px; margin:15px 0;}
.profile-links a {display:inline-flex; gap:8px; align-items:center; padding:9px 11px; border:1px solid #567783; background:#26515b; border-radius:7px; text-decoration:none; color:white !important; font-size:.85rem;}
.profile-links a:hover {background:#116a70;}
.profile-links .mark {width:23px; height:23px; border-radius:5px; background:#e4f5f1; color:#123b45; display:flex; justify-content:center; align-items:center; font-weight:800; font-size:12px;}
</style>''', unsafe_allow_html=True)

st.markdown('<div class="kicker">York, Pennsylvania | Home buying and radon</div>', unsafe_allow_html=True)
st.title("Buying a Home in York, PA? Check the Radon Test Before Closing")
st.markdown('<div class="lead">A home inspection can reveal roof leaks and wiring issues. Radon is different: you cannot see or smell it, so a properly conducted test is the only way to know whether the home has elevated indoor levels.</div>', unsafe_allow_html=True)

st.markdown("""
A buyer looking at a property in York County may receive a stack of documents before settlement. The radon report deserves its own careful review, especially if the house has a basement, an older test on file, or a mitigation system already installed.

For background on local testing and reduction options, see [**Radon Mitigation York, PA**](https://radonmitigationyorkpa.us/). The questions below can help buyers understand what to ask and what evidence to request before deciding on next steps.

## 1. Ask whether a radon test has already been performed

Start by requesting the complete report rather than a verbal assurance that the home passed. Look for the test date, testing method, measurement result in picocuries per liter (pCi/L), testing location, and the name of the person or company who performed it.

A past result is useful background, but it may not reflect the home's present conditions. According to EPA guidance, a buyer may want a new test when the previous result is not recent, testing conditions were not followed, or the property has changed since the test.

## 2. Check which part of the home was tested

The testing location matters. If you plan to turn a basement into a bedroom, home office, or living room, a first-floor measurement alone may not answer your question about that lower space.

Ask where the device was placed and whether the location follows the applicable testing protocol. The EPA specifically notes that buyers may request tests on a lower level they intend to occupy, even when the seller's earlier test was conducted elsewhere.

## 3. Plan the test early in the transaction

Radon testing can become a last-minute complication when everyone is focused on inspections, financing, and closing paperwork. Discuss timing with your real estate agent and a Pennsylvania-certified radon testing professional as early as practical.

For short-term testing, the tester should follow the required closed-building and device-placement protocols. Do not move the testing device, leave windows open contrary to instructions, or assume a rushed or invalid measurement provides a reliable answer.

## 4. Review the result in context

The EPA recommends fixing a home at **4 pCi/L or above** and considering a reduction when the result is between **2 and 4 pCi/L**. These are action guidelines, not a guarantee that lower readings carry no risk.

If a result is elevated, discuss confirmation testing and mitigation options with an appropriately certified professional. Whether additional testing is appropriate, and what kind, depends on the measurement and the testing circumstances.

## 5. If the house already has a mitigation system, request documentation

A visible pipe and fan do not prove that the indoor radon concentration is low. Request the installation details, available warranty or service records, and post-installation radon test results.

Ask whether the fan and monitoring indicator are functioning as intended. Arrange an independent radon measurement when appropriate. An operating indicator is useful for monitoring pressure, but it does not measure indoor radon.

## 6. Consider changes made since the last test

A previous radon report may predate finished-basement work, foundation repairs, HVAC alterations, or other building changes. Such work can change airflow or soil-gas entry pathways.

Ask about these changes before deciding to rely on an older result. A new test may be sensible even when an earlier report showed a comparatively low concentration.

## 7. What to request before closing

- A copy of any radon testing report, including dates and locations.
- Details of any installed radon reduction system.
- Post-mitigation results, if a system was installed.
- Information about major renovations since the last test.
- The qualifications of the testing or mitigation professional.
- A clear plan for additional testing or correction if necessary.

These are practical questions for the property review process, not a substitute for contract advice. Your agent or attorney can explain how inspection terms, disclosures, and any agreed repairs work in your particular transaction.

## Frequently asked questions

### Does a house without a basement need radon testing?

Yes. Radon can enter buildings with slabs, crawl spaces, and other foundation types. Testing is recommended regardless of whether a home has a basement.

### Can I use my neighbor's radon test result?

No. Homes close to one another can have different concentrations. Only a test in the property you are buying can tell you about that property's measured radon level.

### Is a radon mitigation system a reason to reject a property?

Not necessarily. Radon can often be reduced with an appropriately designed mitigation system. The important questions are whether the system was professionally installed, whether it works, and what follow-up test results show.

### Should the buyer request a new test if the seller already tested?

Possibly. The age of the report, location of testing, testing conditions, and changes to the property all matter. Review the report with a qualified testing professional.

## Final takeaway

Radon belongs on a York home buyer's checklist alongside the other inspection items. Get the report, confirm where and when the home was tested, ask about any reduction system, and rely on qualified testing rather than assumptions about the neighborhood.

**Official resources:** [EPA Home Buyer's and Seller's Guide to Radon](https://www.epa.gov/radon/home-buyers-and-sellers-guide-radon) and [Pennsylvania DEP: Radon in the Home](https://www.pa.gov/agencies/dep/programs-and-services/radiation-protection/radon-division/radon-in-the-home).
""")

profiles = [
    ("X", "X", "https://x.com/radonmitigation"),
    ("Facebook", "f", "https://www.facebook.com/radonmitigationyorkpa/"),
    ("EZlocal", "EZ", "https://ezlocal.com/pa/york/radon-mitigation-services/0919852194"),
    ("Manta", "M", "https://www.manta.com/c/m1h2ygb/radon-mitigation-york-pa"),
    ("MerchantCircle", "MC", "https://www.merchantcircle.com/radon-mitigation-york-pa-york-pa"),
    ("Houzz", "H", "https://www.houzz.com/pro/radonmitigationyork/radon-mitigation-york"),
    ("Pinterest", "P", "https://www.pinterest.com/radonmitigationyorkpa/"),
    ("TikTok", "♪", "https://www.tiktok.com/@radonmitigationyorkpa"),
]
links = ''.join(
    f'<a href="{escape(url, quote=True)}" target="_blank" rel="noopener noreferrer" aria-label="{escape(name)}">'
    f'<span class="mark" aria-hidden="true">{escape(icon)}</span>{escape(name)}</a>'
    for name, icon, url in profiles
)
st.markdown(
    '<div class="footer"><h3>Find Radon Mitigation York, PA</h3>'
    '<p>Social profiles and local business listings</p>'
    f'<nav class="profile-links" aria-label="Social and business profiles">{links}</nav>'
    '<p style="font-size:.82rem;margin-bottom:0">Educational guide for York, Pennsylvania home buyers. For an individual property, consult qualified radon professionals and applicable real estate advisers.</p></div>',
    unsafe_allow_html=True,
)
