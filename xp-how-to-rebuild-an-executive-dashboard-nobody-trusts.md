I’ve written before about the thinking behind a dashboard rebuild: trace one wrong number down to the raw record, pick one methodology, validate it three ways. This is the companion piece. It’s the plan, in the order I’d run it, for when an executive dashboard has lost the room and someone has asked you to fix it.

The temptation is to open the BI tool and start redesigning. Resist it. A dashboard loses trust because of what’s underneath it, and the rebuild has to start there too.

## Phase one: stop the bleeding

Before anything else, stop the damage. Take the numbers people have caught being wrong off the page, or put a visible note on them saying they’re under review. Freeze changes to the existing tiles so nobody is debugging a moving target. Then tell the readers what you’re doing and roughly how long it will take.

This feels like admitting failure. It’s the opposite. A tile that says “under review” is more trustworthy than one that keeps asserting a figure everyone in the room knows is off.

## Phase two: interview the readers

Sit down with each person who reads the dashboard, one at a time. Ask three things. Which numbers do you actually look at? Which decisions do you make from them? What do you check them against? The third question matters most. Every reader has a second source they trust more, and that source tells you what the dashboard has to reconcile to before anyone will believe it.

You’ll also learn which tiles nobody reads. Those don’t get rebuilt. A rebuild is the one time you can remove things without a fight.

## Phase three: inventory every number and its source

Make a list. For each number on the dashboard: where the data comes from, which table or query produces it, who built it, what filters it carries, and when it last changed. Most of the list will be blank at first. Filling it in is the real work of the rebuild, and it’s where you find the duplicated logic, the stale filters, and the two tiles that look identical but read from different places.

Keep the inventory somewhere people can see it. It becomes the documentation nobody had before.

## Phase four: pick the single methodology

With the inventory in hand, you’ll find the same metric defined several ways. Pick one. Write the definition in plain language: what counts, what’s excluded, which date it keys on, which currency, which time zone. Get finance and the business owner to agree to it in writing before you build anything.

When you can’t get agreement, keep both definitions, give them different names, and never let them share a tile. Disagreement is tolerable. Ambiguity is not.

## Phase five: rebuild in code, with tests

Build the new version as code: SQL in version control, a script that deploys through the BI tool’s API, and tests that run before every deploy. The tests don’t need to be clever. Row counts against the source. Period totals against the ledger. A check that no record falls outside the period it’s reported in. A check that the data is fresher than the tolerance you agreed on.

Each failing test is a conversation you get to have before the readers have it for you.

## Phase six: relaunch with a changelog and an owner

Launch the new version next to the old one, not instead of it. Publish a changelog that lists every number that moved and why. Put an owner’s name on the dashboard, with a way to report a problem. Keep the old version around until people have stopped comparing.

Trust comes back slowly, and only if the dashboard behaves the same way every week. The owner’s job from here is boring on purpose: keep the tests green, keep the changelog current, and answer questions before they turn into rumors.

None of these phases is technically hard. The hard part is doing them in order, and not shipping a prettier version of the same untrusted numbers.

---

*Originally published at [malekdamiri.com](https://malekdamiri.com/writing/how-to-rebuild-an-executive-dashboard-nobody-trusts/).*
