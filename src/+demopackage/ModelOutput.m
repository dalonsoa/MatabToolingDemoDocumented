classdef ModelOutput
    % MODELOUTPUT Result returned by demopackage.runModel

    properties (SetAccess = immutable)
        % Intensity of the model
        intensity (:, 1) double
    end

    methods

        function obj = ModelOutput(intensity)
            % MODELOUTPUT Construct the model output
            %
            % Args:
            %   intensity (double): Intensity value to be stored in the model
            arguments
                intensity (:, 1) double
            end

            obj.intensity = intensity;
        end

    end
end
