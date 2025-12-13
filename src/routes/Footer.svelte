<script>
  import Column from "./Column.svelte";
  import Logo from "./Logo.svelte";
  import Fa from "svelte-fa/src/fa.svelte";
  import { faEnvelope } from "@fortawesome/free-solid-svg-icons";

  const year = new Date().getFullYear();
</script>

<div class="bg-white">
  <Column class="pt-10 pb-10">
    <div class="flex flex-col-reverse justify-between gap-4 items-center md:flex-row md:items-start">
      <div>
        <Logo />
        <p class="mt-4">Not just any software, your software</p>
        <p>&copy; {year} Gadget Technologies LLC</p>
      </div>
    </div>
  </Column>
  <Column>
  <section id="commerce-disclosure">
      <h2>Commerce Disclosure (Notation Based on the Act on Specified Commercial Transactions)</h2>
      <table>
          <tr>
              <th>Legal Name</th>
              <td>Sanath Sambamoorthi</td>
          </tr>
          <tr>
              <th>Address</th>
              <td>Disclosed Upon Request</td>
          </tr>
          <tr>
              <th>Phone Number</th>
              <td>Disclosed Upon Request</td>
          </tr>
          <tr>
              <th>Email</th>
              <td>me@sanath-sambamoorthi.com</td>
          </tr>
          <tr>
              <th>Website</th>
              <td>https://sanath-sambamoorthi.com</td>
          </tr>
          <tr>
              <th>Product/Service Prices</th>
              <td>Prices are as listed on the site or quoted individually. All prices exclude taxes and fees unless stated.</td>
          </tr>
          <tr>
              <th>Additional Fees</th>
              <td>None</td>
          </tr>
          <tr>
              <th>Payment Methods</th>
              <td>Credit/debit cards via Stripe, Cash, Wise Transfer</td>
          </tr>
          <tr>
              <th>Delivery Timing</th>
              <td>Custom work timing is agreed with customer based on the request. Consulting should be received within 7 business days depending on customer schedule.</td>
          </tr>
          <tr>
              <th>Return/Exchange Policy</th>
              <td>Cancellation with refund is available up to 24 hours before session for coaching/consulting. Defective work will be fixed on request at no additional charge up to 21 days after delivery.</td>
          </tr>
          <tr>
              <th>Payment Period</th>
              <td>Payment period	Period that customers are expected to make payments.	Credit card payments are processed immediately, while local bank transfers must be sent within 3 days of the date of order.</td>
          </tr>
          <tr>
              <th>Price Sales</th>
              <td>Dependent on scope of work agreed on with the client</td>
      </table>
      <p>This disclosure is provided in accordance with Japan's Specified Commercial Transactions Act. Last updated: December 13, 2025.</p>
  </section>
  </Column>
</div>
