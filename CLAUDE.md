# Read this before anything else

This repository is the source of truth. Any account of it in a chat, a PDF, a
memory file or an earlier message in this conversation is stale by default.

## Entry protocol

Run these four commands before answering any question about this project,
including one that looks small:

```
cat docs/STATE.md
cat docs/decisions.md
cat docs/claims.md
git log --oneline -10
```

`docs/decisions.md` indexes every binding decision with a pointer into
`docs/evaluation-protocol.md`. The protocol is 830 lines of rule, rationale,
rejected alternative and history; the index is the part that binds.

## Hard rules

1. **Do not answer a question about how a case is scored without having read
   `docs/decisions.md` in this session.** On 2026-10-03 three settled
   questions were reopened — the renal composite under rule 3, the potassium
   denominator under rule 4, and the Q1/Q2/Q3 requirement under rule 2 — by
   grepping the protocol instead of reading the index. Two of them are settled
   in the protocol by name, citing the very output under review.

2. **Do not conclude that a document lacks a provision from grep output.**
   Open the section and read it. grep returns lines; rules live in paragraphs,
   and a truncated paste looks exactly like an absent rule.

3. **Do not run a git write operation through an agent shell in this
   repository** — no add, commit, push, checkout, gc, or anything else that
   writes to `.git`. It leaves `.git/*.lock` files that only the user can
   remove, and it has blocked her working tree before. Reads, file writes and
   `pipeline/check_claims.py` are fine. Hand her the commit command instead.

4. **Read `docs/credentials.md` before any command that could touch a key.**
   Never grep for a secret's pattern: the match prints the secret. That
   mistake has been made four times in this project, once by an agent.

5. **Run `python3 pipeline/check_claims.py` after editing any document** and
   before reporting the edit as done. It is the mechanical guard on
   cross-document claims.

6. **Check `docs/decisions.md` before proposing a rule, a panel size, a code,
   a metric or a denominator.** Most are already decided, several against
   alternatives that were considered and rejected for recorded reasons.

## What this is

A hallucination-detection pipeline for clinical trial lay summaries under EU
CTR 536/2014 Annex V. Stages 1 and 2 run; stage 0 does not exist. No metric
has been computed on the final panel and no result is reported — statements to
the contrary are errors, and `check_claims.py` enforces that.

The author is a physician who had not written Python before September 2026.
Explain mechanism, not syntax, and do not simplify the statistics.
