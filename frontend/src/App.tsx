export default function App() {
  return (
    <div className="flex w-full flex-col items-center justify-center gap-8 p-4">
      <h1 className="text-4xl">The Batch Searcher</h1>
      <div className="relative flex w-full max-w-xl items-center">
        <div className="absolute top-0 left-4 z-10 flex h-full items-center text-xl text-slate-500">
          <svg
            stroke="currentColor"
            fill="none"
            stroke-width="2"
            viewBox="0 0 24 24"
            stroke-linecap="round"
            stroke-linejoin="round"
            data-sentry-element="FiSearch"
            data-sentry-source-file="SearchBox.tsx"
            height="1em"
            width="1em"
            xmlns="http://www.w3.org/2000/svg"
          >
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
        </div>
        <input
          type="search"
          placeholder="Search here..."
          className="relative h-16 w-full rounded-lg border-slate-300 px-4 py-0 pl-12 text-base leading-none text-neutral-800 shadow-sm focus:border-none focus:outline-none"
        />
      </div>
    </div>
  );
}
