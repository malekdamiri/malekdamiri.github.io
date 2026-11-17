Every company has a metric dictionary. In most of them it lives in people’s heads, in the SQL behind the dashboards, and in the slide where a number was last explained. Writing it down is not documentation for its own sake. It means the next argument about a number can be settled by reading instead of by meeting.

## What a metric dictionary is

One entry per metric, in plain language, readable by someone in finance, sales, or data without translation. It is not a data catalog, which lists tables and columns. It is not a dashboard inventory. It sits above both and answers three questions: what does this metric mean, who decides, and where does the number come from.

If a metric is not in the dictionary, it is not a metric yet. It is a query someone ran.

## The fields each entry needs

Eight fields cover almost everything.

1.  **Name.** One canonical name, plus the aliases people actually use so the entry can be found.
2.  **Definition.** One or two sentences on what it measures and what it excludes.
3.  **Formula in words.** Not SQL. A sentence a non-technical reader can check against the SQL.
4.  **Owner.** A person, the one who decides what the metric means and signs off on changes.
5.  **Source of truth.** Which system, and which table or report inside it, wins when sources disagree.
6.  **Grain.** What one row represents: per customer per month, per deal, per invoice line.
7.  **Refresh.** How often the number updates and how to tell when it last did.
8.  **Known gaps.** What the number does not capture, which cases are handled by hand, and where it is known to drift.

The last field is the most useful and the least often written. A metric with its gaps listed is one people trust more, not less, because they can see that someone has looked.

## A few example entries

Bookings. Definition: contract value of opportunities closed-won in the period. Formula: sum of the amount on closed-won opportunities by close date, net of discounts. Owner: sales operations lead. Source of truth: the CRM opportunity object. Grain: one row per opportunity. Refresh: nightly. Known gaps: amendments after close are not reflected unless the opportunity is reopened.

Recognized revenue. Definition: revenue earned in the period under the company’s recognition policy. Formula: as published by finance at close. Owner: the controller. Source of truth: the general ledger, fed by billing. Grain: one row per customer per month. Refresh: monthly, after close. Known gaps: not available before close, and any pre-close estimate is labeled as an estimate.

Active customer. Definition: a customer with at least one paid invoice in the trailing window. Formula: count of distinct billing customer IDs with a paid invoice in the trailing window. Owner: RevOps. Source of truth: billing, joined to the account mapping table. Grain: one row per customer per day. Refresh: daily. Known gaps: customers on unpaid pilots are excluded, and parent and child accounts count once.

These are generic on purpose. Yours will differ in every detail. The shape is the point.

## Source-of-truth rules

A metric has exactly one source of truth. Other systems can hold copies, and the dictionary should say they are copies. The rule I use is that the system where a fact is created owns it. Deals are created in the CRM, so the CRM owns bookings. Invoices are created in billing, so billing owns billings and revenue. The warehouse creates nothing. It joins.

That makes the warehouse the source of truth only for derived metrics, the ones that need both systems to exist. Even then, the entry names which upstream system wins when the two disagree, so a conflict has an answer before it happens.

## How to keep it alive

A dictionary dies the day it stops matching the dashboards. Three habits keep it current. Every dashboard tile links to its dictionary entry, and a tile without an entry does not ship. Every change to a definition goes through the owner and leaves a note in the entry saying what changed and from which period. Once a quarter, each owner confirms their entries are still right or fixes them. An entry nobody will own gets deleted, because if nobody owns it, nobody should be reporting it.

Keep it somewhere with history. Plain text in a repository works well. A wiki works if someone tends it. A spreadsheet works until there are two copies of it.

The dictionary will not end disagreements. It changes what they are about. Instead of arguing over whose number is right, people argue over whether the definition is right, and that is an argument you can actually finish.

The slides for this essay are on Speaker Deck: [The RevOps metric dictionary](https://speakerdeck.com/malekdamiri/the-revops-metric-dictionary-by-malek-damiri).

---

*Originally published at [malekdamiri.com](https://malekdamiri.com/writing/revops-metric-dictionary/). More from Malek Damiri on revenue operations at [malekdamiri.com](https://malekdamiri.com/).*
