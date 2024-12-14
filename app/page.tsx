"use client";

import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";

export default function IndexPage() {
  const [msg, setMsg] = useState("");
  const [diamonds, setDiamonds] = useState<string | null>(null);
  const [highscore, setHighscore] = useState<string | null>(null);
  const [lastRiskTime, setLastRiskTime] = useState<number>(0);

  useEffect(() => {
    const storedDiamonds = localStorage.getItem("diamonds") || "0";
    setDiamonds(storedDiamonds);
    const storedHighscore = localStorage.getItem("highscore") || "0";
    setHighscore(storedHighscore);
  }, []);

  const saveDiamondsToLocalStorage = (value: string) => {
    localStorage.setItem("diamonds", value);
    setDiamonds(value);
  };

  const saveHighscoreToLocalStorage = (value: string) => {
    localStorage.setItem("highscore", value);
    setHighscore(value);
  };

  function riskDiamond(numberOfDiamonds: number) {
    const currentTime = Date.now();

    if (currentTime - lastRiskTime < 500) {
      setMsg("Please wait a second before trying again.");
      return;
    }

    setLastRiskTime(currentTime);

    if (!diamonds) return;
    const parsedDiamonds = parseInt(diamonds);
    const riskFactor = numberOfDiamonds / 100;

    if (Math.random() < riskFactor) {
      setMsg("You got caught and lost all your diamonds!");
      saveDiamondsToLocalStorage("0");
    } else {
      const newDiamonds = String(parsedDiamonds + numberOfDiamonds);
      setMsg(`You successfully robbed a bank with ${numberOfDiamonds} diamond${numberOfDiamonds > 1 ? "s" : ""}!`);
      saveDiamondsToLocalStorage(newDiamonds);
      if (parseInt(newDiamonds) > parseInt(highscore || "0")) {
        saveHighscoreToLocalStorage(newDiamonds);
      }
    }
  }

  if (diamonds === null) {
    return <p>Loading...</p>;
  }

  return (
    <section className="container grid items-center gap-6 pb-8 pt-6 md:py-10">
      <div className="flex max-w-[980px] flex-col items-start gap-2">
        <h1 className="text-3xl font-extrabold leading-tight tracking-tighter md:text-4xl">
          Diamond Risk
        </h1>
        <p className="max-w-[700px] text-lg text-muted-foreground">
          Try to steal as many diamonds without getting caught
        </p>
      </div>
      <p>Highscore: {highscore}</p>
      <p>Diamonds: {diamonds}</p>
      <p>{msg}</p>
      <p>Rob a bank with:</p>
      <div className="flex gap-4 flex-wrap">
        <Button onClick={() => riskDiamond(1)}>1 diamond</Button>
        <Button onClick={() => riskDiamond(5)}>5 diamonds</Button>
        <Button onClick={() => riskDiamond(10)}>10 diamonds</Button>
        <Button onClick={() => riskDiamond(20)}>20 diamonds</Button>
        <Button onClick={() => riskDiamond(50)}>50 diamonds</Button>
      </div>
    </section>
  );
}

