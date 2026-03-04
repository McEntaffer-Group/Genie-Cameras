% --- Settings ---
exposure_us = 34;   % exposure time in microseconds
gain_dB     = 1.0;     % gain in dB
save_dir    = 'C:\Users\jad507\OneDrive - The Pennsylvania State University\Pictures\Reverse Telescope Test\20260304\genieshots';  % change this
interval_s  = 60;      % seconds between frames

% --- Setup ---
if ~exist(save_dir, 'dir'), mkdir(save_dir); end

%vid = videoinput('gige', 1, 'Mono8');
%src = getselectedsource(vid);
% Safe cleanup before creating new src
if exist('src','var') && isvalid(src)
    try
        delete(src);
    catch
        % delete may fail; ignore or handle as needed
    end
end
clearvars src
src = gigecam;
src.ExposureTime = exposure_us;
src.Gain         = gain_dB;
pause(1)
fprintf('Acquiring every %d seconds. Press Ctrl+C to stop.\n', interval_s);

frame_num = 1;
while true
    %frame    = getsnapshot(vid);
    frame = snapshot(src);

    t = datetime('now','Format','yy-MM-dd HH-mm-ss');
    fname = sprintf('image_%04d %s.png', frame_num, char(t));
    filename = fullfile(save_dir, fname);
    %filename = fullfile(save_dir, sprintf('image_%04d.png', frame_num));
    imwrite(frame, filename);
    fprintf('[%s] Saved %s\n', datestr(now,'HH:MM:SS'), filename);
    frame_num = frame_num + 1;
    pause(interval_s);
end