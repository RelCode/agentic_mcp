# Testing Prompts for Agentic MCP

Use these example documents to exercise different parts of the pipeline.
They are ordered from **riskiest** to **safest** based on expected overall
risk score (more issues and older legislation → riskier).

---

## 1. High Risk – Multiple Old Acts, No Disclaimer or Scope

**Risk level:** High (riskiest)

```text
This tax advisory note concerns the treatment of capital allowances for small businesses operating in the retail and professional services sectors. The purpose of this memorandum is to summarise the historic and current rules on annual investment allowance (AIA) and writing-down allowances, as applied to the client’s fixed asset base, including fixtures, fittings, IT equipment and certain refurbishments carried out over the last decade.

The analysis is based on the Finance Act 2012, Finance Act 2014 and Finance Act 2016, with reference to the Income Tax (Trading and Other Income) Act 2005 and related HMRC guidance in place at the time. In particular, we refer to the AIA limits that applied in the 2013/14, 2014/15, 2015/16 and 2016/17 tax years, as well as the transitional rules that governed expenditure straddling changes in those limits.

Under the assumptions adopted in this note, the annual investment allowance is treated as if the higher temporary limits introduced in those historic years remain available for the client’s current period of account. The client may therefore claim relief on qualifying expenditure incurred in those years, even where the statutory filing deadlines have already passed. We have also assumed that no restrictions apply under anti-avoidance provisions, and that there are no connected parties or group arrangements that might reduce the available AIA.

The document does not explicitly set out the scope of work and does not explain whether matters such as VAT, PAYE compliance, stamp taxes, or the interaction with corporation tax loss reliefs are covered. No distinction is made between advice on historic periods and advice on current and future transactions. There is no clear statement identifying which jurisdictions are considered and whether non-UK tax consequences have been reviewed.

No statement is included to limit the adviser’s liability or to clarify that the advice is based on legislation and HMRC practice in force at the time the note was prepared. The note does not explain that subsequent changes to the Finance Act 2020, Finance Act 2021 or later legislation might render the conclusions inaccurate. It also does not highlight any need for the client to obtain updated advice if their facts change, if they acquire or dispose of additional assets, or if HMRC publishes new guidance that narrows the scope of reliefs claimed.

The client is encouraged to rely on the calculations and illustrative examples set out in the appendices without any visible warning that those examples are simplified and may not capture all relevant tax adjustments. In several places, the memorandum uses definitive language such as "the client will be entitled" and "this treatment is correct in all circumstances" without acknowledging that alternative interpretations may exist or that HMRC could challenge the position.
```

**Why risky:**
- References legislation/tax years before 2020 → likely flagged as outdated.
- No clear disclaimer.
- No clear scope of work.

---

## 2. Medium Risk – Mixed Years, Ambiguous Disclaimer and Scope

**Risk level:** Medium

```text
This memorandum summarises the capital gains tax (CGT) consequences of disposing of residential property held by an individual who is both UK-resident and domiciled. It is intended to provide a high-level overview of how main residence relief, lettings relief and the 30-day CGT reporting and payment regime might apply to the client’s portfolio of properties. The note is prepared on the basis of information supplied informally by the client and has not been independently verified.

References are made to the Finance Act 2010, Finance Act 2015 and Finance Act 2019, as well as changes introduced for the 2020/21 and 2021/22 tax years. In particular, we discuss the historic rules governing the final period exemption, the withdrawal of certain lettings relief provisions, and the introduction of the 30-day reporting requirements for UK residential property disposals. Examples are included that assume specific acquisition and disposal dates spanning the period from 2011 to 2022.

We have reviewed the client’s position under the main residence relief rules on the assumption that the property in question has been occupied as the client’s only or main residence for part, but not all, of the period of ownership. We touch briefly on periods of absence, periods of letting to third parties, and short-term occupation patterns. High-level calculations are provided to illustrate how chargeable gains might be computed under both the pre-2015 rules and the post-2019 rules.

The document contains general statements to the effect that the content is "for guidance only" and is "not intended to be a substitute for professional advice in all circumstances." However, it does not clearly state whether it is a formal opinion addressed to the client, nor does it indicate whether the advice can be relied upon for filing tax returns or dealing with HMRC enquiries. No clear, prominent limitation of liability clause is included, and there is no express statement about the intended audience beyond the named client.

The memorandum does not specifically set out the scope of work or identify which taxes, time periods or jurisdictions are outside scope. It briefly mentions that inheritance tax and stamp duty land tax could also be relevant but does not confirm that these have been reviewed. There is no explicit confirmation that overseas tax rules, double tax treaties or non-resident CGT regimes have not been considered. The boundaries of the engagement are therefore left open to interpretation.

No explicit limitation of liability or governing law clause has been included, and there is no detailed warning that tax law can change and that the conclusions may be affected by future Finance Acts or case law. While some references are made to legislative changes in 2020/21 and 2021/22, the note does not systematically distinguish between rules that apply before and after key change dates, which may create uncertainty about how the guidance should be applied to specific historic disposals.
```

**Why medium risk:**
- Mix of pre-2020 and post-2020 years → some potentially outdated.
- Disclaimer language is vague.
- Scope of work is not clearly defined.

---

## 3. Low Risk – Recent Acts, Clear Disclaimer and Scope

**Risk level:** Low (safest)

```text
This legal opinion addresses the application of the Finance Act 2023 and the Income Tax Act 2022 to dividends paid to UK-resident individual shareholders in the 2023/24 tax year. It has been prepared at the request of ABC Limited (the "Company") for the sole purpose of analysing the UK income tax consequences of a proposed dividend distribution from retained profits arising in its most recent accounting period.

Scope of work: This opinion covers only the UK income tax and dividend tax consequences of the proposed transaction. It does not address corporation tax implications for the Company, the interaction with any loss reliefs, controlled foreign company rules, transfer pricing, or any aspect of VAT, stamp taxes, employment taxes, social security contributions or non-UK tax considerations. Unless expressly stated otherwise, this opinion does not consider the position of any shareholders who are not individuals, including corporate entities, partnerships or trustees.

In preparing this opinion, we have assumed that all shareholders are individuals who are domiciled and resident in the UK for all relevant tax years, and that they hold their shares beneficially and not as nominees. We have also assumed that there are no relevant anti-avoidance provisions in point beyond those described in this opinion, that the Company is not party to any arrangements designed to secure a tax advantage, and that the proposed dividend is funded from distributable reserves in accordance with applicable company law.

Disclaimer: This opinion is provided solely for the use of the Company and may not be relied upon by any other person without our prior written consent. It is based on UK tax law (including published HMRC practice) in force as at 1 April 2024 and does not take into account any changes to legislation, case law, HMRC practice or other authority after that date. We accept no responsibility or liability to any third party who may come into possession of this opinion. Our conclusions may change if the relevant legislation is amended or if the underlying facts or assumptions differ from those set out above.

We have reviewed the dividend allowance and the basic, higher and additional rate bands for the 2023/24 tax year, and we provide illustrative calculations showing the effective rates of tax for shareholders in each band. We also outline, at a high level, how the personal allowance and other sources of income can interact with dividend income in determining the final tax liability. However, we do not model every possible scenario, and the numerical examples are for illustration only.

For the avoidance of doubt, this opinion does not constitute advice on the wider financial planning context of the shareholders, nor does it cover the suitability of distributing profits by way of dividend versus salary or bonus. We recommend that shareholders seek independent financial advice if they wish to consider those issues. If the Company contemplates alternative forms of distribution, such as share buy-backs or capital reductions, further advice should be sought as the tax consequences may differ materially.

The note explains that, where there is any doubt about the application of the legislation to a specific set of facts, the Company or the affected shareholders may wish to approach HMRC for a clearance or informal view. It also recommends that the Company keeps appropriate documentation regarding the declaration and payment of dividends, including board minutes and shareholder approvals, to support the tax treatment adopted.
```

**Why low risk:**
- Uses recent legislation and tax years (post‑2020).
- Contains an explicit, strong disclaimer.
- Clearly defines the scope of work.
