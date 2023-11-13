defmodule MyModule do
  @lose "X"
  @draw "Y"
  @win "Z"
  def main do
    m = %{
      ["A", @lose] => 3 + 0,
      ["B", @lose] => 1 + 0,
      ["C", @lose] => 2 + 0,
      ["A", @draw] => 1 + 3,
      ["B", @draw] => 2 + 3,
      ["C", @draw] => 3 + 3,
      ["A", @win] => 2 + 6,
      ["B", @win] => 3 + 6,
      ["C", @win] => 1 + 6
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
