<script>
  import Column from "./Column.svelte";
  import Logo from "./Logo.svelte";
  import Fa from "svelte-fa/src/fa.svelte";
  import { faEnvelope } from "@fortawesome/free-solid-svg-icons";
  const year = new Date().getFullYear();

  let showDisclosure = false; // Reactive variable to toggle disclosure visibility
</script>

<footer class="bg-white py-10"> <!-- Added py-10 for vertical padding; adjust as needed -->
  <Column>
    <div class="flex flex-col-reverse justify-between gap-6 items-center md:flex-row md:items-start">
      <div class="text-center md:text-left"> <!-- Centered on mobile, left on desktop -->
        <Logo />
        <p class="mt-4 text-gray-600">Not just any software, your software</p>
        <p class="text-sm text-gray-500">
          &copy; {year} Gadget Technologies LLC | 
          <a 
            href="#commerce-disclosure" 
            class="text-blue-600 hover:underline" 
            on:click|preventDefault={() => showDisclosure = !showDisclosure}
          >
            Commerce Disclosure
          </a>
        </p>
      </div>
    </div>
    <section id="commerce-disclosure" class="mt-8 p-4 bg-gray-50 rounded-lg border border-gray-200"> <!-- Styled container for better visuals -->
      {#if showDisclosure}
        <h2 class="text-xl font-semibold mb-4">Commerce Disclosure (Notation Based on the Act on Specified Commercial Transactions)</h2>
        <div class="overflow-x-auto"> <!-- Makes table responsive on mobile -->
          <table class="min-w-full border-collapse border border-gray-300">
            <tr>
              <th class="border border-gray-300 px-4 py-2 bg-gray-100 text-left font-medium">Legal Name</th>
              <td class="border border-gray-300 px-4 py-2">Sanath Sambamoorthi</td>
            </tr>
            <tr>
              <th class="border border-gray-300 px-4 py-2 bg-gray-100 text-left font-medium">Address</th>
              <td class="border border-gray-300 px-4 py-2">Disclosed Upon Request</td>
            </tr>
            <tr>
              <th class="border border-gray-300 px-4 py-2 bg-gray-100 text-left font-medium">Phone Number</th>
              <td class="border border-gray-300 px-4 py-2">Disclosed Upon Request</td>
            </tr>
            <tr>
              <th class="border border-gray-300 px-4 py-2 bg-gray-100 text-left font-medium">Email</th>
              <td class="border border-gray-300 px-4 py-2">me@sanath-sambamoorthi.com</td>
            </tr>
            <tr>
              <th class="border border-gray-300 px-4 py-2 bg-gray-100 text-left font-medium">Website</th>
              <td class="border border-gray-300 px-4 py-2">https://sanath-sambamoorthi.com</td>
            </tr>
            <tr>
              <th class="border border-gray-300 px-4 py-2 bg-gray-100 text-left font-medium">Product/Service Prices</th>
              <td class="border border-gray-300 px-4 py-2">Prices are as listed on the site or quoted individually. All prices exclude taxes and fees unless stated.</td>
            </tr>
            <tr>
              <th class="border border-gray-300 px-4 py-2 bg-gray-100 text-left font-medium">Additional Fees</th>
              <td class="border border-gray-300 px-4 py-2">None</td>
            </tr>
            <tr>
              <th class="border border-gray-300 px-4 py-2 bg-gray-100 text-left font-medium">Payment Methods</th>
              <td class="border border-gray-300 px-4 py-2">Credit/debit cards via Stripe, Cash, Wise Transfer</td>
            </tr>
            <tr>
              <th class="border border-gray-300 px-4 py-2 bg-gray-100 text-left font-medium">Delivery Timing</th>
              <td class="border border-gray-300 px-4 py-2">Custom work timing is agreed with customer based on the request. Consulting should be received within 7 business days depending on customer schedule.</td>
            </tr>
            <tr>
              <th class="border border-gray-300 px-4 py-2 bg-gray-100 text-left font-medium">Return/Exchange Policy</th>
              <td class="border border-gray-300 px-4 py-2">Cancellation with refund is available up to 24 hours before session for coaching/consulting. Defective work will be fixed on request at no additional charge up to 21 days after delivery.</td>
            </tr>
            <tr>
              <th class="border border-gray-300 px-4 py-2 bg-gray-100 text-left font-medium">Payment Period</th>
              <td class="border border-gray-300 px-4 py-2">Payment period Period that customers are expected to make payments. Credit card payments are processed immediately, while local bank transfers must be sent within 3 days of the date of order.</td>
            </tr>
            <tr>
              <th class="border border-gray-300 px-4 py-2 bg-gray-100 text-left font-medium">Price Sales</th>
              <td class="border border-gray-300 px-4 py-2">Dependent on scope of work agreed on with the client</td>
            </tr>
          </table>
        </div>
        <p class="mt-4 text-sm text-gray-600">This disclosure is provided in accordance with Japan's Specified Commercial Transactions Act. Last updated: December 13, 2025.</p>
      {/if}
    </section>
  </Column>
</footer>
