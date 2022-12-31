<script>
  export let title = '';
  export let text = '';
  export let color = '';
</script>

<div class={`bg-white flex flex-col justify-between items-center border-2 border-transparent hover:border-${color} rounded-2xl shadow-md p-10 gap-4 text-center`}>
  <div>Icon</div>
  <h3>{title}</h3>
  <p>{text}</p>
  <div class={`w-36 h-[2px] bg-${color}`}></div>
</div>
