import React, { useEffect, useRef, useState } from "react";
import ChatBubble from "./components/ChatBubble";

type ListItem = {
  id: number;
  text: string;
  isUser: boolean;
};

export default function App() {
  const [messages, setMessages] = useState<ListItem[]>([]);
  const [errorString, setErrorString] = useState<string | undefined>(undefined);
  const [responseLoading, setResponseLoading] = useState(false);
  const inputRef = useRef<HTMLInputElement | null>(null);
  const buttonRef = useRef<HTMLButtonElement | null>(null);

  const handleScrollToBottom = () => {
    window.scrollTo({ top: 200000, behavior: "smooth" });
  };

  useEffect(() => {
    handleScrollToBottom();
  }, [messages]);

  useEffect(() => {
    if (responseLoading) {
      clearInput();
      disableForm();
    } else {
      enableForm();
    }
  }, [responseLoading]);

  const makeAPIQuery = async (inputText: string, backendURL: string) => {
    setResponseLoading(true);
    try {
      const response = await fetch(`${backendURL}/converse`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ query: inputText }),
      });
      const data = await response.json();
      const { response: botResponse } = data;
      const { output } = botResponse;
      return output;
    } catch (error) {
      setErrorString(
        "An serverside error has occured. Please refresh the page or try again later.",
      );
    } finally {
      setResponseLoading(false);
    }
  };

  function disableForm() {
    if (inputRef.current) {
      inputRef.current.disabled = true;
    }
    if (buttonRef.current) {
      buttonRef.current.disabled = true;
    }
  }
  function enableForm() {
    if (inputRef.current) {
      inputRef.current.disabled = false;
    }
    if (buttonRef.current) {
      buttonRef.current.disabled = false;
    }
  }

  function clearInput() {
    if (inputRef.current) {
      inputRef.current.value = "";
    }
  }

  const formOnSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const form = event.currentTarget;
    const inputValue = form.querySelector("input") as HTMLInputElement;
    const inputText = inputValue.value;

    if (!inputText) return;
    const backendURL = import.meta.env.VITE_BACKEND_URL;
    if (!backendURL) {
      setErrorString("Backend URL is not defined");
      enableForm();
      return;
    }
    if (inputText.length < 5) {
      setErrorString("Query is too short");
      enableForm();
      return;
    }
    if (inputText.length > 100) {
      setErrorString("Query is too long");
      enableForm();
      return;
    }
    setErrorString(undefined);

    setMessages((prevValue: ListItem[]) => [
      ...prevValue,
      {
        id: prevValue.length + 1,
        text: inputText,
        isUser: true,
      },
    ]);

    const queryResponse = await makeAPIQuery(inputText, backendURL);
    if (queryResponse) {
      setMessages((prevValue: ListItem[]) => [
        ...prevValue,
        {
          id: prevValue.length + 1,
          text: queryResponse,
          isUser: false,
        },
      ]);
    }
  };

  return (
    <div className="flex w-full flex-col items-center justify-center gap-8 p-4">
      <h1 className="text-4xl">The Batch Searcher</h1>

      <div
        id="messages-list"
        className="-z-10 flex w-full max-w-2xl flex-col gap-4 pb-38 sm:pb-24"
      >
        {messages.map((message) => (
          <ChatBubble message={message} key={`item-${message.id}`} />
        ))}
        {responseLoading && (
          <span className="italic">Loading your answer...</span>
        )}
        {errorString && <span className="italic">{errorString}</span>}
      </div>
      <form
        className="fixed bottom-0 z-10 flex w-full max-w-2xl flex-col gap-4 border border-r-transparent border-b-transparent border-l-transparent bg-white py-6 sm:flex-row sm:gap-2"
        onSubmit={formOnSubmit}
        onKeyDown={(e) => {
          e.key === "Enter" && e.preventDefault();
        }}
      >
        <input
          ref={inputRef}
          className="w-full rounded-sm border border-b-cyan-800 px-4 py-2"
          type="text"
          placeholder="What are some news about Brain2Qwerty?"
        />
        <button
          ref={buttonRef}
          className="cursor-pointer rounded-sm border border-b-cyan-800 px-4 py-2"
          type="submit"
        >
          Send
        </button>
      </form>
    </div>
  );
}
