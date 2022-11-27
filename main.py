#!/usr/bin/env python
import logging

import snecs.bound_world
import tcod

import g


def main() -> None:
    tileset = tcod.tileset.load_tilesheet("data/dejavu16x16_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    with tcod.context.new(
        tileset=tileset,
        width=1280,
        height=720,
        title=None,
        vsync=True,
    ) as g.context:
        g.world = snecs.bound_world.BoundWorld()
        while True:
            console = g.context.new_console()
            console.print(0, 0, "Hello world.")
            g.context.present(console, keep_aspect=True, integer_scaling=True)
            for event in tcod.event.wait():
                match event:
                    case tcod.event.Quit():
                        raise SystemExit()


if __name__ == "__main__":
    if __debug__:
        logging.basicConfig(level=logging.DEBUG)
    main()