<script>
  import Fa from "svelte-fa/src/fa.svelte";

  export let icon;
  export let title = '';
  export let text = '';
</script>

<div class="bg-transparent text-white flex flex-col justify-between items-center border-2 border-white hover:border-cyan-500 rounded-lg shadow-lg shadow-cyan-900 p-10 gap-4 text-center">
  <div class="text-4xl">
    <Fa icon={icon} />
  </div>
  <h3 class="font-bold text-2xl">{title}</h3>
  <p>{text}</p>
  <div class="w-[50%] h-[2px] bg-cyan-500"></div>
</div>
