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
</div>
