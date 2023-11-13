{:ok, file} = File.open("../input.txt", [:read])

contents = IO.read(file, :all) |> String.split("\n\n")

lists =
  Enum.map(contents, fn section ->
    section
    |> String.split("\n")
    |> Enum.map(&String.to_integer/1)
    |> Enum.sum()
  end)

Enum.max(lists) |> IO.puts()

File.close(file)
