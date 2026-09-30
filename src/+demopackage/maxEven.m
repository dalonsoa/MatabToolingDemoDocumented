function max_even = maxEven(vals)
    % Return the maximum even number in an array
    %
    % Takes the input array, filters out odd values and returns the maximum
    %
    % Args:
    %   vals (array double): Array of values to take the maximum from.
    %
    % Returns:
    %   (double) Maximum value
    arguments (Input)
        vals
    end

    arguments (Output)
        max_even
    end

    even_vals = vals(mod(vals, 2) == 0);
    max_even = max(even_vals);
end
