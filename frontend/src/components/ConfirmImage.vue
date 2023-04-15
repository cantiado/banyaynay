<script setup>
    import Button from './Button.vue'
</script>

<template>
    <div class="p-5 flex flex-col justify-between">
        <div>
            <h2 class="text-2xl">Confirm Image</h2>
            <h3 class="text-center text-xl mt-5">Is this image okay?</h3>
        </div>
        <div class="justify-center">
                
            <div class="flex justify-center">
                <img src="../assets/logo.svg" width="75" />
            </div>
            
        </div>
        <div class="flex justify-between">
                <Button txt="Use a different image" />
                <Button txt="Yes, banyaynay-ify" />
        </div>   
    </div>
</template>