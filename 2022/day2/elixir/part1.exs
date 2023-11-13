defmodule MyModule do
  @rock "X"
  @paper "Y"
  @scissors "Z"
  def main do
    m = %{
      ["A", @rock] => 1 + 3,
      ["B", @rock] => 1 + 0,
      ["C", @rock] => 1 + 6,
      ["A", @paper] => 2 + 6,
      ["B", @paper] => 2 + 3,
      ["C", @paper] => 2 + 0,
      ["A", @scissors] => 3 + 0,
      ["B", @scissors] => 3 + 6,
      ["C", @scissors] => 3 + 3
    }

    contents =
      File.read!("../input.txt") |> String.split("\r\n") |> Enum.filter(fn line -> line != "" end)

    total =
      Enum.reduce(contents, 0, fn line, acc ->
        [opponent, player] = String.split(line, " ")
        result = Map.get(m, [opponent, player])
        acc + result
      end)

    IO.puts(total)
  end
end

MyModule.main()
