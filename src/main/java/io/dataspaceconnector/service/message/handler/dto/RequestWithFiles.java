/*
 * Copyright 2020-2022 Fraunhofer Institute for Software and Systems Engineering
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package io.dataspaceconnector.service.message.handler.dto;

import de.fraunhofer.iais.eis.Message;
import lombok.AllArgsConstructor;
import lombok.Data;

/**
 * Implementation of the {@link RouteMsgWithFiles} interface for requests.
 * Should contain a subclass of either {@link de.fraunhofer.iais.eis.RequestMessage} or
 * {@link de.fraunhofer.iais.eis.NotificationMessage} as header and can contain an arbitrary
 * payload and files.
 *
 * @param <H> the header type.
 * @param <B> the body/payload type.
 * @param <C> the jwt claims.
 * @param <F> the files.
 */
@Data
@AllArgsConstructor
public class RequestWithFiles<H extends Message, B, C, F> extends Request<H, B, C> implements RouteMsgWithFiles<H, B, F> {
    /**
     * The header.
     */
    private final H header;

    /**
     * The body/payload.
     */
    private final B body;

    /**
     * The jwt claims.
     */
    private final C claims;

    /**
     * The files of a multipart/form-data request
     */
    private final F files;
}
