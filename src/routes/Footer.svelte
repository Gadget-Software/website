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
      <a
        href="mailto:sanath@gadget-software.tech"
        class="shadow border-[1px] border-gray-200 hover:border-cyan-500 rounded-lg flex justify-between items-center gap-4 p-4">
        <span class="text-2xl">
          <Fa icon={faEnvelope} />
        </span>
        Send us an email<br />sanath@gadget-software.tech
      </a>
    </div>
  </Column>
</div>
