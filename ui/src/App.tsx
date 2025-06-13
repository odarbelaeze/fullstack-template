import { Button } from "./components/ui/button";
import { useState } from "react";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="grid min-h-dvh place-items-center">
      <div className="flex flex-col items-center gap-2">
        <h1>Vite + React + Tailwind + Shadcn</h1>
        <Button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </Button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
    </div>
  );
}

export default App;
