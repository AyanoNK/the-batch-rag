import React, { useEffect, useRef, useState } from "react";

type ListItem = {
  id: number;
  text: string;
  isUser: boolean;
};

const li: ListItem[] = [
  {
    id: 1,
    text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatibus.",
    isUser: true,
  },
  {
    id: 2,
    text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatibus.",
    isUser: false,
  },
  {
    id: 3,
    text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatibus.",
    isUser: true,
  },
  {
    id: 4,
    text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatibus.",
    isUser: false,
  },
  {
    id: 5,
    text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatibus.",
    isUser: true,
  },
];
export default function App() {
  const [items, setItems] = useState<ListItem[]>(li);

  const handleScrollToBottom = () => {
    window.scrollTo({ top: 10000, behavior: "smooth" });
  };

  useEffect(() => {
    handleScrollToBottom();
  }, [items]);

  const formOnSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const form = event.currentTarget;
    const inputValue = form.querySelector("input") as HTMLInputElement;
    const inputText = inputValue.value;

    if (!inputText) return;

    setItems((prevValue: ListItem[]) => [
      ...prevValue,
      {
        id: prevValue.length + 1,
        text: inputText,
        isUser: true,
      },
      {
        id: prevValue.length + 2,
        text: "This is a magical response! It is not real, but it is magical!",
        isUser: false,
      },
    ]);
  };

  return (
    <div className="flex w-full flex-col items-center justify-center gap-8 p-4">
      <h1 className="text-4xl">The Batch Searcher</h1>

      <div
        id="messages-list"
        className="-z-10 flex w-full max-w-2xl flex-col gap-4 pb-24"
      >
        {items.map((item) => (
          <div
            key={`item-${item.id}`}
            className={`flex w-full justify-${item.isUser ? "end" : "start"}`}
          >
            <div
              className={`max-w-md rounded-t-lg ${item.isUser ? "rounded-bl-lg" : "rounded-br-lg"} border border-b-cyan-800 p-4`}
            >
              <span>{item.text}</span>
            </div>
          </div>
        ))}
      </div>
      <form
        className="fixed bottom-0 z-10 flex w-full max-w-2xl flex-col gap-4 border border-r-transparent border-b-transparent border-l-transparent bg-white py-6 sm:flex-row sm:gap-2"
        onSubmit={formOnSubmit}
      >
        <input
          className="w-full rounded-sm border border-b-cyan-800 px-4 py-2"
          type="text"
        />
        <button
          className="cursor-pointer rounded-sm border border-b-cyan-800 px-4 py-2"
          type="submit"
        >
          Send
        </button>
      </form>
    </div>
  );
}
