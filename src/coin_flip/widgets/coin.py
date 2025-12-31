from textual.app import ComposeResult
from textual.widgets import Label, Static
from textual.containers import Vertical
from random import choice
import asyncio

class Coin(Vertical):

    flip_count, heads_count, tails_count = 0, 0, 0
    outcomes = ['heads','tails']


    def compose(self) -> ComposeResult:
        yield Static(id="coin_state")
        with Vertical(id="counter_group"):
            yield Label(id="flip_count", classes="counter")
            yield Label(id="heads_count", classes="counter")
            yield Label(id="tails_count", classes="counter")

    def on_mount(self) -> None:
        self.query_one("#coin_state", Static).update("○ ○ ○")
        self.query_one("#flip_count", Label).update(f"Flips made: {self.flip_count}")
        self.query_one("#heads_count", Label).update(f"[green]Heads[/]: {self.heads_count}")
        self.query_one("#tails_count", Label).update(f"[red]Tails[/]: {self.tails_count}")


    async def flip_coin(self) -> None:
        frames = ["○", "○ ○", "○ ○ ○"]
        for frame in frames:
            await asyncio.sleep(0.5)
            self.query_one("#coin_state", Static).update(frame)
        
        out = choice(self.outcomes)

        if out == "heads":
            text = "[green]Heads[/]"
            self.heads_count += 1
            self.query_one("#heads_count", Label).update(f"[green]Heads[/]: {self.heads_count}")
        else:
            text = "[red]Tails[/]"
            self.tails_count += 1
            self.query_one("#tails_count", Label).update(f"[red]Tails[/]: {self.tails_count}")
        
        
        self.flip_count += 1
    

        self.query_one("#coin_state", Static).update(text)
        self.query_one("#flip_count", Label).update(f"Flips made: {self.flip_count}")