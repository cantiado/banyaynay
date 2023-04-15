<script setup>
    import Button from './Button.vue';
</script>

<template>
    <div class="p-5 flex flex-col justify-between">
        <h2 class="text-2xl">Image upload</h2>
        <div class="justify-center">
            <h3 class="text-center text-xl">Choose a picture:</h3>
            <div class="flex justify-center">
                <input type="file" accept="image/png, image/jpeg">
            </div>
        </div>
        <div class="flex justify-between">
            <Button txt="Back" />
            <Button txt="Submit" />
        </div>
    </div>
</template>