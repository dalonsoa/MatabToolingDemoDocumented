function max_odd = maxOdd(vals)
    % Return the maximum odd number in an array
    %
    % Takes the input array, filters out even values and returns the maximum
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
        max_odd
    end

    odd_vals = vals(mod(vals, 2) != 0);
    max_odd = max(odd_vals);
end
