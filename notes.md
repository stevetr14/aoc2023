seeds: 79 14 55 13

Example:
seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

First line:
- Source: 98 -> 98, 99
- Destination: 50 -> 50, 51
- Range length: 2

So 98 -> 50, 99 -> 51

Second line:
- Source: 50 -> 50, 51, 52, 53, ..., 96, 97
- Destination: 52 -> 52, 53, 54, 55, ..., 98, 99
- Range length: 48

So 50 -> 52, 51 -> 53, 52 -> 54, 53 -> 55, ..., 97 -> 99

Unmapped: 0 to 49

So 0 -> 0, ..., 49 -> 49

Therefore, seed 79 -> soil 81, seed 14 -> soil 14, seed 55 -> soil 57, seed 13 -> soil 13


Start with 99 (match 50 98 2)
- Destination < source
- Seed > Range
- Source > range
- 98 <= 99 <= 99 so Yes => 99 (Seed) - 98 (Source) + 50 (Destination) = 51
- 51 -> 36 -> 25 -> 18 -> 18 -> 19 -> 19

Fertiliser with soil 14 (match 39 0 15):
- Destination > source
- Source < range
- Seed < range
- 0 <= 14 <= 14 so 14 (Seed) - 0 (Source) + 39 (Destination) = 53

Temperature with light 74 (match 68 64 13)
- Destination > source
- Seed > range
- Source > range
- 64 <= 74 <= 76 so 74 (Seed) - 64 (Source) + 68 (Destination) = 78

Test case 36 (match 330 30 160)
- Destination > source
- Source < range
- Seed < range
- Seed > Source
- 30 <= 36 <= 189 so 36 (Seed) - 30 (Source) + 330 (Destination) = 336

Test case 49 (match 18 25 70)
- Destination < source
- Source < range
- Seed < range
- 49 (Seed) - 25 (Source) + 18 (Destination) = 42


Part 2:
Seeds 79 14 55 13 => (79, 14), (55, 13)
[79, 80, 81, 82, 83, ..., 91, 92]

Seed 82 from first pair has the lowest location number.


seed-to-soil map:
50 98 2
52 50 48 -> 93 91

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

93 93

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

93 93

water-to-light map:
88 18 7
18 25 70  -> 86 93

0 17

light-to-temperature map:
45 77 23 -> 54 86
81 45 19
68 64 13
0 44

temperature-to-humidity map:
0 69 1
1 0 69 -> 55 54

humidity-to-location map:
60 56 37
56 93 4

0 55 -> 55
