<style lang="scss">
  // See for reference: https://greduan.com/blog/2022/06/27/tailwind-grid-cols-mx-auto
  .column {
    @apply mx-auto w-full max-w-screen-2xl grid grid-cols-12;

    &.wider {
      @apply max-w-screen-3xl;

      & > .left,
      & > .right {
        @apply md:col-span-1 lg:col-span-1;
      }

      & > .middle {
        @apply px-2 md:px-0 col-span-full md:col-span-10 lg:col-span-10;
      }
    }

    & > .left,
    & > .right {
      @apply md:col-span-1 lg:col-span-2;
    }

    & > .middle {
      @apply px-4 md:px-0 col-span-full md:col-span-10 lg:col-span-8;
    }
  }
</style>

<script lang="ts">
  export let contentClass = '';
  let className = '';
  export { className as class };
  export let wider = false;
</script>

<div class={`column ${className}`} class:wider={wider}>
  <div class="left"></div>
  <div class={`middle ${contentClass}`}>
    <slot />
  </div>
  <div class="right"></div>
</div>
