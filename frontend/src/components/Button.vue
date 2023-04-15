<script setup>
defineProps({
  txt: {
    type: String,
    required: true
  }
})
</script>

<template>
    <button type="button" class="rounded-md bg-pink border-black border-2 w-fit h-fit px-5 py-2">{{ txt }}</button>
</template>