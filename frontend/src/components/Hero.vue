<script setup>
import Button from './Button.vue'
</script>

<template>
    <div class="bg-img flex flex-col items-center p-5 gap-20 ">
        <div class="p-10"></div>
        <h2 class="p-10 text-9xl text-center bg-amber-200 rounded-lg drop-shadow-2xl">Want to find out if ___ is part banana?</h2>
        <Button txt="Get started!" />
    </div>
</template>

<style scoped>
.bg-img {
    background-image: url("../assets/b4.jpg");
    background-size: cover;
}
</style>