% this script attempts to connect a Dalsa Genie to Matlab and the Image
% Processessing Toolbox and Support Package for GigE Vision Hardware
% rather than the Teledyne provided SDK/libraries (which would need to be
% programmed in C or C++ or something else. This seems to be the way that
% the previous gui used it. If you run into problems, it may be that MATLAB
% does not have windows defender permissions to access the network, so you
% will need admin privileges to give it access.
%see also https://www.mathworks.com/matlabcentral/answers/1645495-dalsa-nano-gige-connection-with-image-acquisition-toolbox

tout = 0.5;
exposure0 = 9000;
timeoutSeconds = 15;
t = waitForGigecamlist(timeoutSeconds, 0.5);

if isempty(t)
        disp('No GigE Vision cameras detected.');
else
    camera = gigecam;
    camera.Timeout = tout;
    camera.ExposureTime = exposure0;  % Set the camera exposure time
    img = snapshot(camera);            % Acquire a single frame from the camera
    figure();                            % Create a new figure window
    imshow(img, []);                  % Display the acquired image
    title("Acquired Image at baseline exposure time " + exposure0);
 % Set the title for the image
end
% Check if the camera is connected and ready
if isvalid(camera)
    % Set the exposure time and display the image using the defined function
    imgs = showExposureGrid(camera, 35, 12000); % ExposureTime should be between 34 and 119979.
else
    disp('Camera is not valid or not connected.');
end
if isobject(camera)
    delete(camera)
    clear camera
end

function t = waitForGigecamlist(timeoutSec, pollInterval)
% waitForGigecamlist  Poll gigecamlist until a camera appears or timeout.
%   T = waitForGigecamlist(TIMEOUTSEC) polls every 0.5 s by default.
%   T = waitForGigecamlist(TIMEOUTSEC, POLLINTERVAL) uses custom interval.
%
%   Returns the table from gigecamlist (empty if timed out).

if nargin < 2 || isempty(pollInterval)
    pollInterval = 0.5; % seconds
end
if nargin < 1 || isempty(timeoutSec)
    timeoutSec = 10;    % default timeout
end

tStart = tic;
t = table(); % default empty
while toc(tStart) < timeoutSec
    try
        t = gigecamlist;
    catch ME
        warning('gigecamlist failed: %s', ME.message);
        t = table(); % treat as no cameras found this poll
    end
    if ~isempty(t)
        return; % found at least one camera
    end
    pause(pollInterval);
end
% timed out; return empty table
end


function imgs = showExposureGrid(camera, minExp, maxExp)
% showExposureGrid  Capture and display a 3x3 grid of images at different exposures.
%   IMGS = showExposureGrid(CAMERA) reads CAMERA.ExposureTimeRange (if present)
%   to get [minExp maxExp], otherwise errors.
%
%   IMGS = showExposureGrid(CAMERA, MINEXP, MAXEXP) uses the provided limits.
%
%   IMGS is a 3x3 cell array of captured images.

% Input checks
if nargin < 1
    error('Camera object required.');
end
if ~isobject(camera) || ~isprop(camera, 'ExposureTime')
    error('First input must be a camera object with an ExposureTime property.');
end

% Determine min/max exposures
if nargin < 3
    % Try common property name
    if isprop(camera, 'ExposureTimeRange')
        range = camera.ExposureTimeRange;
    elseif isprop(camera, 'ExposureTimeLimits')
        range = camera.ExposureTimeLimits;
    else
        error(['Provide min and max exposures, or ensure the camera object ' ...
               'has ExposureTimeRange or ExposureTimeLimits property.']);
    end
    minExp = range(1);
    maxExp = range(2);
else
    if ~isnumeric(minExp) || ~isnumeric(maxExp) || minExp >= maxExp
        error('Provide numeric minExp < maxExp.');
    end
end

% Create 9 evenly spaced exposure values
n = 9;
exposures = linspace(minExp, maxExp, n)

% Prepare output
imgs = cell(3,3);

% Create figure
fig = figure('Name', 'Exposure Grid', 'NumberTitle', 'off');

for k = 1:n
    expVal = exposures(k);
    try
        camera.ExposureTime = expVal;
    catch ME
        warning('Failed to set ExposureTime = %g: %s', expVal, ME.message);
        % continue with previous exposure if set failed
    end

    pause(0.05);            % allow setting to take effect; increase if needed
    img = snapshot(camera); % acquire frame
    imgs{k} = img;

    % Display in 3x3 subplot
    subplot(3,3,k);
    if ndims(img) == 2
        imshow(img, []);
        colormap(gca, gray(256));
    else
        imshow(img);
    end
    axis image off;
    title(sprintf('Exposure = %g', expVal), 'Interpreter', 'none');

    drawnow;
end

end



function img = setExposureAndShow(camera, exposureTime)
% setExposureAndShow  Set camera ExposureTime, acquire one frame, and show it.
%   IMG = setExposureAndShow(CAMERA, EXPOSURETIME) sets the ExposureTime
%   property of the gigecam/videoinput object CAMERA to EXPOSURETIME (numeric),
%   takes one snapshot, displays it with appropriate scaling, and returns the image.
%
%   Example:
%     cam = gigecam;
%     img = setExposureAndShow(cam, 150000);

% Basic input checks
if nargin < 2
    error('Two inputs required: camera object and numeric exposureTime.');
end
if ~isobject(camera) || ~isprop(camera, 'ExposureTime')
    error('First input must be a camera object with an ExposureTime property.');
end
if ~isnumeric(exposureTime) || ~isscalar(exposureTime)
    error('ExposureTime must be a numeric scalar.');
end

% Set exposure (wrap in try to catch property errors)
try
    camera.ExposureTime = exposureTime;
catch ME
    error('Failed to set ExposureTime: %s', ME.message);
end

% Small pause to allow camera to apply setting (adjust if needed)
pause(0.05);

% Acquire and display
img = snapshot(camera);

figure;
if ndims(img) == 2
    imshow(img, []);         % auto-scale grayscale / single-channel
    colormap(gca, gray(256));
else
    imshow(img);             % RGB
end
axis image off;
title(sprintf('ExposureTime = %g', exposureTime), 'Interpreter', 'none');
end