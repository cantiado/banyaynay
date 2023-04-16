<script setup>
import Button from './Button.vue'
</script>

<template>
    <div class="bg-img flex flex-col items-center justify-center p-5 pb-20 sticky top-0 h-screen">
        <div class="px-8 py-8 mx-10 mt-10 bg-amber-200 rounded-lg drop-shadow-2xl flex flex-col items-center gap-10">
            <h2 class=" text-8xl text-center ">Want to find out if ___ is part banana?</h2>
            <!-- <Button txt="Get started!" /> -->
            <a href="#banyaynay-ify"><button type="button" class="rounded-md bg-magenta w-fit h-fit px-5 py-3 text-xl">Get started!</button></a>
        </div>
        
    </div>
</template>

<style scoped>
.bg-img {
    background-image: url("../assets/b4.jpg");
    background-size: cover;
}
</style>