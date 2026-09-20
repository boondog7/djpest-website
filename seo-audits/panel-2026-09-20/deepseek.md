Note: I could not browse the live competitor URLs in this session. Competitor comparisons below are based on the packet plus known patterns for Flick, Rentokil, Jim’s and Allpest, and should be re-verified against current live pages.

## 1. FIRST-GLANCE VERDICT

A stressed homeowner at 9pm sees the dark screen load fast, the top bar “Perth’s northern suburbs · Warwick-based · Family-run since 2011,” and the emotional headline “Rats in the roof tonight? We fix it properly, and put it in writing” with a visible Call button; that is better than most small pest sites. They are likely to call if the page fully loads, because the offer is direct and local. But the first screen has no real photo, no visible proof or review, and the footer/licence status may create hesitation after the initial click; trust is not yet established at first glance.

## 2. TOP 10 CHANGES, ranked by expected impact on phone calls

### 1. Rodent page hero: delete “WA licence 13914”

- **Exact page/element:** `/rodent-control-perth.html`, hero bullet list under the H1.
- **What is wrong:** It breaks the owner’s hard constraint: “the technician holds a PROVISIONAL licence under supervision (say ‘licensed technicians’, never a licence number).” It is also a public licence-number disclosure that is unverifiable and could create a WA Health (Pesticides) Regulations 2011 issue.
- **Precise fix:** Replace the bullet with:
  > Licensed technicians under WA Health (Pesticides) Regulations 2011

  Do not publish technician licence numbers anywhere public. Licence details belong only on the customer’s private treatment record.
- **Confidence:** [high]

### 2. Home hero: rewrite the above-the-fold subhead and CTA ordering

- **Exact page/element:** `index.html`, hero H1/subhead/buttons.
- **What is wrong:** The H1 is strong for rodent emergencies, but the subhead leads with “run by a Chartered Accountant,” which is a differentiator but not a first-glance reason to call. The customer at 9pm wants speed, local proof, price fairness, and a written record.
- **Precise fix:** Keep the emotional H1 but tighten the subhead and CTA priority:
  > **H1:** Rats in the roof tonight? We can usually be there today.
  >
  > **Subhead:** Warwick-based licensed pest control for Perth’s northern suburbs. Itemised written price before we start, written treatment record after, and a re-treatment promise you can read before booking.
  >
  > Primary CTA: **Call 0447 747 769**  
  > Secondary CTA: **Get a fair price**
- **Confidence:** [high]

### 3. Pricing guide: add a direct-answer snippet at the very top

- **Exact page/element:** `/pest-control-prices-perth.html`, directly below the H1.
- **What is wrong:** The page currently opens with “Here is what we charge, before you call,” then tables. It is good, but it does not give a one-glance answer for the query “How much does pest control cost Perth?”
- **Precise fix:** Paste this under the H1, formatted as a normal paragraph, not an image:
  > For a standard 3-bedroom home in Perth’s northern suburbs, a general pest treatment typically costs $250–$350 inc. GST, a termite inspection $250–$350, and a termite chemical management system $2,500–$5,500 depending on construction. Every job is quoted itemised in writing; no call-out fee, no deposit.

  Add `Speakable` schema around this block.
- **Confidence:** [high]

### 4. Whole site: replace stock/illustrative photos with real job or equipment photos

- **Exact page/element:** Home hero, service pages, suburb pages, commercial page.
- **What is wrong:** Currently “stock/illustrative photos only,” which is a severe trust gap for pest control. Homeowners want to see a real station, a real roof void, a real redback web or termite damage.
- **Precise fix:** Take real photos on the first few jobs: tamper-resistant rodent station in place, termite damage, mud tubes, redback web, roof void entry gaps, the treatment report printed, the vehicle/uniform without faces or names if needed. Use them on relevant pages, with descriptive