# My final project: a first idea (week 7)

Name:

Date:

Answer each part in your own words: two or three sentences is enough.
Under each heading is the **wind turbine's** answer, as an example. Delete
it once you have written yours. Rough is fine today. If you have two ideas,
copy the headings again and write both.

## 1. Ask: the question

What do you want to know or decide? Who has this problem: you, someone you
know, a club, a place you work?

> Turbine: which blades, pitch and fan set-up give the most voltage from a
> classroom kit, without cutting and testing every option by hand?

## 2. Measure: the real thing

What can you measure yourself, with things you already own: a phone, a
timer, a ruler, a kitchen scale, a spreadsheet you keep? How long does one
measurement take, and can you repeat it?

> Turbine: a voltmeter across the motor, and a phone filming the rotor in
> slow motion at 240 frames a second. One measurement is about six seconds
> of video and one meter reading, and it can be repeated any time.

## 3. Model: what the agent would build

What would you ask the agent to make: a simulation, a calculator, a tool
that sorts or reads your data, a dashboard? Say it in one sentence a friend
would understand.

> Turbine: a physics model of the blades, gears, motor and fan, plus a 3D
> dashboard to try a set-up before building it. Opus 5.5 wrote the code
> and its 23 tests.

## 4. Calibrate and check: is it true?

Which measurement would you use to tune the model? Which **different**
measurement would show whether it is right? (A run you used for tuning
cannot also be the test. It will agree, because you made it agree.)

> Turbine: one run (316 rpm at 6.83 V) set the motor's volts per rpm and
> the fan's real wind speed. The check was a different run: a group
> measured about 7 V, best near 9° of pitch, and the blades needed a flick
> to start. The model says 6.8 to 6.9 V, best at 9°, needs a flick. Not
> yet measured: the friction in the gears.

## 5. Decide: what would you do differently?

Once the model works, what decision does it help you make?

> Turbine: keep the kit's 10″ blades (the model's best is 9⅞″), not the
> 14″ ones, which lose 15%. To start without a flick, use 4 blades or a
> steeper pitch.

## 6. What stays private

What in this project is personal or belongs to someone else: names, faces,
places, money, health, a workplace's records? How will you keep it out of
your repository, and out of a cloud model?

> Turbine: a person was visible through a window in the background of the
> video. The frames on the class slides were cropped to the turbine.

## 7. Compared with the turbine

Read the windTurbine repository: its README (especially *Calibration and
assumptions*) and its commit history. Name one thing your idea has that the
turbine had, and one thing it is missing.

## What could stop it?

Be honest: no way to measure it, too big, it needs equipment or data you do
not have. What would make it smaller?
