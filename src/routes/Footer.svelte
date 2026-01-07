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
            href="/commerce-disclosure" 
            class="text-blue-600 hover:underline" 
          >
            Commerce Disclosure
          </a>
        </p>
      </div>
    </div>
  </Column>
</footer>
