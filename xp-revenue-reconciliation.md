Finance closes the month from the billing system. Sales reports from the CRM. The analytics team builds its dashboards from the warehouse. Three systems, three revenue numbers, and a recurring argument about which one is right.

Usually none of them is wrong. They measure different things at different moments. The problem is that nobody has written down which number is for what, so every gap looks like an error. This is the operating model I’d put in place to make reconciliation a routine instead of a fight.

## Three systems, three jobs

The billing system is the record of what was invoiced and collected. The CRM is the record of what was sold and what is expected to close. The warehouse joins the two, keeps history, and is where the analysis happens.

Each is authoritative for something and none is authoritative for everything. Billing owns invoiced and recognized revenue. The CRM owns bookings and pipeline. The warehouse owns nothing on its own. It owns the reconciliation between the other two and the reporting built on top. When the warehouse disagrees with billing about revenue, billing wins. When it disagrees with the CRM about what was booked, the CRM wins. Saying that out loud once saves a lot of meetings.

## Who owns which number

Every number that reaches an executive deck needs one owner, a person rather than a team. Finance owns revenue. Sales operations owns bookings. RevOps owns the mapping between them: which closed-won deal became which invoice, and which CRM account is which billing customer.

That mapping is the real work. Deals and invoices rarely line up one to one. A deal becomes several invoices, an invoice covers several deals, an account gets renamed in one system and not the other. Keep the mapping as its own table in the warehouse, owned by one person, and treat every unmapped record as a task with a due date.

## A monthly cadence

Reconciliation that happens when someone notices a gap is too late. Put it on the calendar and tie it to the close.

In the first few business days after month end, finance closes billing and publishes recognized revenue by customer. Over the next few days, RevOps pulls bookings from the CRM and invoices from billing, joins them in the warehouse, and produces the variance report. By the end of the following week, the open items have been reviewed, the disputes settled, and the report signed off by both owners.

Monthly is the minimum. For large deals I’d also check bookings against invoicing weekly, because a big contract that never gets invoiced is the kind of gap you want to find in week one, not at close.

## Tolerance thresholds

Not every gap deserves a ticket. Decide in advance what counts as a difference worth chasing, and set it two ways: an absolute amount and a percentage, at the customer level and at the total level. A small timing difference on one invoice is noise. The same difference repeated across dozens of customers is a pattern, and the total-level threshold is what catches it.

Both thresholds get written down, agreed by finance and sales operations, and revisited once a year. Anything inside tolerance is logged and left alone. Anything outside gets an owner and a date.

## How disputes get settled

Most disputes fall into three categories. Timing: the deal closed in one month and the invoice went out in the next. Scope: the CRM says one amount and the signed contract says another. Identity: the same customer exists under two names, or two customers share one.

Each category gets a default answer. Timing: the invoice date drives revenue and the close date drives bookings, and both are correct. Scope: the signed contract wins and the CRM is corrected to match. Identity: the billing customer ID is the master and the CRM carries it as a field. When a dispute fits none of the categories, the two owners meet, decide, and the decision becomes a new rule. The goal is that the same argument never happens twice.

## What gets written down

Four things. The variance report itself, every month, archived where anyone can find it. The exception log: each item outside tolerance, its root cause, who fixed it, and how. The rule book: the default answers above plus every rule added since. And the mapping table, with history, so you can see what changed and when.

After a few months the exception log tells you where the process leaks. If most exceptions are identity problems, fix how accounts get created. If most are scope, the CRM amount field needs a control. The log turns reconciliation from cleanup into diagnosis.

None of this is sophisticated, and most of it is not SQL. The hard part is getting two teams to accept that the number each of them produces is right for its purpose and wrong for the other’s. Once that is agreed, reconciliation stops being a monthly argument and becomes a monthly checklist.

The slides for this essay are on Speaker Deck: [Revenue reconciliation: a practical operating model](https://speakerdeck.com/malekdamiri/revenue-reconciliation-a-practical-operating-model-for-finance-and-sales-by-malek-damiri).

---

*Originally published at [malekdamiri.com](https://malekdamiri.com/writing/revenue-reconciliation-operating-model/). More from Malek Damiri on revenue operations at [malekdamiri.com](https://malekdamiri.com/).*
