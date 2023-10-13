<template>
  <header>
    <nav class="border-b border-red-700 ">
      <div class="flex justify-between items-center xl:px-4 xl:py-3 py-2 px-2">
        <div class="xl:ml-10 ml-3 sm:ml-7 flex flex-row gap-2.5 font-mono items-center justify-center text-whitesmoke">
          <a class="hover:text-yellow-500 font-mono"
            ><svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-6 h-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M12 18v-5.25m0 0a6.01 6.01 0 001.5-.189m-1.5.189a6.01 6.01 0 01-1.5-.189m3.75 7.478a12.06 12.06 0 01-4.5 0m3.75 2.383a14.406 14.406 0 01-3 0M14.25 18v-.192c0-.983.658-1.823 1.508-2.316a7.5 7.5 0 10-7.517 0c.85.493 1.509 1.333 1.509 2.316V18"
              />
            </svg>
          </a>
          <a class="xl:text-2xl text-lg font-rale hover:text-red-500" href=""> WARMONGER:CRAWLER</a>
        </div>
        <div class="xl:mr-10 xl:text-xl text-base mr-2">
          <ul class="flex flex-row xl:space-x-8 sm:space-x-4 sm:mr-6 space-x-2">
            <li>
              <a
                href="#"
                class="text-whitesmoke font-monster hover:text-gray-300"
                >Обзор БПЛА разных стран</a
              >
            </li>
            <li>
              <a
                href="#/drone_table"
                class="text-red-500 font-monster hover:text-red-400 "
                >База данных малых БПЛА</a
              >
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
export default {};
</script>
