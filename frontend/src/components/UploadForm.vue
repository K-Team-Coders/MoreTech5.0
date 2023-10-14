<template>
  <div class="h-full">
    <div class="px-[150px]">
      <p
        class="text-idealDarkGray flex justify-center text-center text-6xl font-TT_Firs_Neue_Bold font-black h-auto pt-12 tracking-wide"
      >
        UPLOAD FILE
      </p>
      <div class="max-w-6xl mx-auto mt-4">
        <div class="relative mb-4 flex w-full items-stretch">
          <input
            class="relative m-0 -mr-0.5 block w-full min-w-0 flex-auto rounded-l-[7px] border-2 border-solid border-idealBlue bg-whitesmoke bg-clip-padding px-3 py-[0.25rem] text-base font-normal leading-[1.6] text-neutral-700 outline-none transition duration-200 ease-in-out focus:z-[3] focus:border-primary focus:text-neutral-700 focus:shadow-[inset_0_0_0_1px_rgb(59,113,202)] focus:outline-none"
            id="file_input"
            type="file"
          />
          <button
            class="relative z-[2] border-idealBlue rounded-r-[7px] border-2 px-4 py-2 text-sm font-medium font-TT_Firs_Neue_Regular text-whitesmoke bg-idealBlue text-gray-50 transition duration-150 ease-in-out hover:bg-black hover:bg-opacity-5 hover:text-idealBlue focus:outline-none focus:ring-0"
            type="button"
            id="button-addon4"
            data-te-ripple-init
          >
            Загрузить
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
